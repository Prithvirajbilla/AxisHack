from django.http import JsonResponse
import json
import datetime
import urllib
import nameservice
from whois import whois

def account_no(request):
	if request.method == 'POST':
		return JsonResponse({})
	account_no = request.GET.get("q",'')
	if(account_no == ''):
		return JsonResponse({"err":"Please provide a valid account number"})
	if(len(account_no) != 15):
		return JsonResponse({"err":"Please provide a valid account number"})
	return JsonResponse({'account_no':account_no,'name':'3 Musketeers','type':"PVT",
	'address':{'pincode':400072,'address1':'Chandivali Farm Road','address2':'','city':'Mumbai','state':'Maharashtra'}})

def customer_id(request):
	if request.method == 'POST':
		return JsonResponse({})
	cust_id = request.GET.get("q",'')
	if(cust_id == ''):
		return JsonResponse({"err":"Please provide a valid customer id"})
	if(len(cust_id) != 15):
		return JsonResponse({"err":"Please provide a valid customer id"})
	suggestions = nameservice.get_company_information(name)
	return JsonResponse({'account_no':account_no,'name':'3 Musketeers','type':"PUB",
	'address':{'pincode':400001,'address1':'1 Duffer Street','address2':'','city':'Mumbai','state':'Maharashtra'}})

def company_name(request):
	if request.method == 'POST':
		return JsonResponse({})
	name = request.GET.get("name",'')
	if(name == ''):
		return JsonResponse({})
	suggestions = nameservice.get_company_information(name)
	return JsonResponse({'sg':suggestions})

def pincode(request):
	if request.method == 'POST':
		return {}
	pincode = request.GET.get("q",'')
	if(pincode == ''):
		return JsonResponse({})
	suggestions = nameservice.get_pincode_details(pincode)
	return JsonResponse({'sg':json.loads(suggestions)})

def website(request):
	if request.method == 'POST':
		return JsonResponse({})
	website = request.GET.get("q",'')
	if(website == ''):
		return JsonResponse({})
	try:
		status = urllib.urlopen('http://'+website).getcode()
	except IOError:
		status = 404
	domain = whois(website)
	return JsonResponse({'status':status,'name':domain.name,'registrar':domain.registrar,'created':domain.creation_date,'expiry':domain.expiration_date})

def verify(request):
	return JsonResponse({'sg':''})
