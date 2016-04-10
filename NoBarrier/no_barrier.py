#!/bin/env python
# -*- coding: utf8 -*-

import random
import SocketServer

from pyicap import *
import redis
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class ThreadingSimpleServer(SocketServer.ThreadingMixIn, ICAPServer):
    pass

class ICAPHandler(BaseICAPRequestHandler):

    def example_OPTIONS(self):
        self.set_icap_response(200)
        self.set_icap_header('Methods', 'RESPMOD')
        self.set_icap_header('Service', 'PyICAP Server 1.0')
        self.set_icap_header('Preview', '0')
        self.set_icap_header('Transfer-Preview', '*')
        self.set_icap_header('Transfer-Ignore', 'jpg,jpeg,gif,png,swf,flv,css,js,ico,woff,woff2,ttf')
        self.set_icap_header('Transfer-Complete', '')
        self.set_icap_header('Max-Connections', '100')
        self.set_icap_header('Options-TTL', '3600')
        self.send_headers(False)

    def example_RESPMOD(self):
        l = self.enc_req
        url = l[1]
        last_pattern = url[-7:]
        default_lang = "hi"
        if "lang" in last_pattern:
            default_lang = last_pattern[-2:]

        if "css" in url:
            self.no_adaptation_required()

        import requests
        f = requests.get(url)
        html_content = f.text;
        from googleapiclient.discovery import build
        service = build('translate', 'v2',developerKey='AIzaSyCOjRVWseMEJJzjzbZ0WmYWNU0rUa0IMzs')
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        words = soup.get_text().strip().split("\n")
        print words
        new_list = []
        already_exists = []
        redis_host = "localhost"
        redis_port = 6379
        redisPool = redis.ConnectionPool(host=redis_host,port=redis_port)
        resource = redis.Redis(connection_pool=redisPool)
        words.sort(key=len, reverse=True)
        for word in words:
            word = word.strip()
            if word != '' and  not resource.hexists(word,default_lang):
                new_list.append(word)
            if resource.hexists(word,default_lang):
                html_content=html_content.replace(word,resource.hget(word,default_lang))
        print new_list
        if len(new_list)  > 0:
            if len(new_list) > 128:
                new_list = new_list[:128]
            boo = service.translations().list(source='en',target=default_lang,q=new_list).execute()
            if "translations" in boo and len(boo["translations"]) > 0:
                kboo = boo["translations"]
                for i in range(len(kboo)):
                    resource.hset(new_list[i],default_lang,kboo[i]["translatedText"])
                    html_content=html_content.replace(new_list[i],kboo[i]["translatedText"])
        
        soup = BeautifulSoup(html_content, 'html.parser')
        metatag = soup.new_tag('meta')
        metatag.attrs['http-equiv'] = 'Content-Type'
        metatag.attrs['content'] = 'text/html; charset=utf-8'
        soup.head.append(metatag)

        for a in soup.find_all('a', href=True):
            a['href'] = a['href']+"?lang="+default_lang

        self.send_enc_error(500,body=str(soup))
        return

port = 13440

server = ThreadingSimpleServer(('', port), ICAPHandler)
try:
    while 1:
        server.handle_request()
except KeyboardInterrupt:
    print "Finished"


