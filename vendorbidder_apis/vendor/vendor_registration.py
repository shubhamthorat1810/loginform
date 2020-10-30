from django.contrib.auth.models import User
from rest_framework.views import APIView

import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError 
from rest_framework.response import Response

from vendorbidder_apis.serializers.vendor_serializer import VendorProfileSerializer
from vendor.models import VendorProfile


class VendorProfileRegister(APIView):


	def create_vendor(self):
		self._user_instance = User.objects.get(email=self.data['email'])
		_vendor_instance =  VendorProfile.objects.create(auth_user = self._user_instance ,isd = self.data['isd'],phone_no = self.data['phone_no'],
										passwords=self.password ,is_active =True)
		serializer = VendorProfileSerializer (_vendor_instance , data=self.data,partial=True)           
		serializer.is_valid()
		serializer.save()
		return HttpResponse (serializer.data)



	def post(self, request):
		self.data = request.data
		username = '+' + str(self.data['isd']) + str(self.data['phone_no'])
		email = self.data['email']
		print(username)
		if self.data['password'] == self.data['conf_password']:
			self.password = self.data['password']
			self.user_instance = User.objects.create_user(username, email, self.password, is_staff=False, is_active=True)
			return self.create_vendor()
		else:
			return HttpResponse("failed")


class Vendorlogin(APIView):

	def post(self,request):
		self.data = request.data
		_vendor_instance = VendorProfile.objects.get(email=self.data['email'],passwords=self.data['password'])
		print(_vendor_instance)
		return HttpResponse ("True")



#####################################################################################



def vendor_register(request,data):
	print("vendor_register")
	try:
		username = ""
		username = '+' + str(data['isd']) + str(data['phone_no'])
		password = data['password']
		email = data['email']
		user_instance = User.objects.create_user(username, email, password, is_staff=False, is_active=True)
		_user_instance = User.objects.get(email=data['email'])
		_vendor_instance =  VendorProfile.objects.create(auth_user = _user_instance ,isd = data['isd'],phone_no = data['phone_no'],
										passwords=password ,is_active =True)
		serializer = VendorProfileSerializer (_vendor_instance , data=data,partial=True)           
		serializer.is_valid()
		serializer.save()
		return True
	except Exception as e:
		print(e)
		return False

def register(request): 
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
		_status = vendor_register(request,data)
		print(_status)
		if _status == True:
			return render(request, "index.html") 
		else:
			return HttpResponse("failed")	
	else:
		return HttpResponse("failed")


def vendor_login(request,data):
	try:
		_vendor_instance = VendorProfile.objects.get(email=data['email'],passwords=data['password'])
		print("_vendor_instance")
		if _vendor_instance:
			return True
		else :
			return False
	except Exception  as e:
		return HttpResponse (e)


def login(request):
	data = {}
	email = request.POST.get("email",None)
	password = request.POST.get("password",None)
	data = {"email":email, "password":password}
	print(data)
	_status =  vendor_login(request,data)
	if _status == True:
		print("True")
		return HttpResponse ("welcome to vendor world")
	else :
		return HttpResponse ("failed")

def index(request):
	return render (request , "index.html")