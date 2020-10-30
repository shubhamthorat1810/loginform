from django.contrib.auth.models import User
from rest_framework.views import APIView

import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError 
from rest_framework.response import Response

from vendorbidder_apis.serializers.bidder_serializer import BidderProfileSerializer
from bidder.models import BidderProfile



def bidder_register(request,data):
	try:
		username = ""
		username = '+' + str(data['isd']) + str(data['phone_no'])
		password = data['password']
		email = data['email']
		user_instance = User.objects.create_user(username, email, password, is_staff=False, is_active=True)
		_user_instance = User.objects.get(email=data['email'])
		_bidder_instance =  BidderProfile.objects.create(auth_user = _user_instance ,isd = data['isd'],phone_no = data['phone_no'],
										passwords=password ,is_active =True)
		serializer = BidderProfileSerializer (_bidder_instance , data=data,partial=True)           
		serializer.is_valid()
		serializer.save()
		return True
	except Exception as e:
		print(e)
		return False

def registerbidder(request): 
	data = {}
	first_name = request.POST.get("first_name")
	last_name = request.POST.get("last_name")
	email = request.POST.get("email")
	isd = request.POST.get("isd")
	phone_no = request.POST.get("phone_no")
	passwords = request.POST.get("password")
	conf_password = request.POST.get("conf_password")
	data = {"first_name":first_name,"last_name":last_name,"email":email,"isd":isd,"phone_no":phone_no,"password":passwords ,"conf_password":conf_password}
	print(data)
	if data['password'] == data['conf_password']:
		_status = bidder_register(request,data)
		print(_status)
		if _status == True:
			return render(request, "index.html") 
		else:
			return HttpResponse("failed")	
	else:
		return HttpResponse("failed")


def bidder_login(request,data):
	try:
		_bidder_instance = BidderProfile.objects.get(email=data['email'],passwords=data['password'])
		print("_bidder_instance")
		if _bidder_instance:
			return True
		else :
			return False
	except Exception  as e:
		return HttpResponse (e)


def loginbidder(request):
	data = {}
	email = request.POST.get("email",None)
	password = request.POST.get("password",None)
	data = {"email":email, "password":password}
	print(data)
	_status =  bidder_login(request,data)
	if _status == True:
		print("True")
		return HttpResponse ("welcome to bidder world")
	else :
		return HttpResponse ("failed")
