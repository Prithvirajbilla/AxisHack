#!/bin/bash
sudo apt-get install squid3
sudo apt-get install build-essential
sudo apt-get install tcl8.5
wget http://download.redis.io/releases/redis-stable.tar.gz
tar xzf redis-stable.tar.gz
cd redis-stable && make && make test && sudo make install

