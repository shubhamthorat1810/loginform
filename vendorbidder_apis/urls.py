from django.urls import path


from vendorbidder_apis.vendor.vendor_registration import VendorProfileRegister , Vendorlogin , register , index , login
from vendorbidder_apis.bidder.bidder_api import  registerbidder ,  loginbidder


urlpatterns = [
	path('', index),
    path('registerbidder/', register , name='registerbidder'),
    path('loginbidder/', login , name='loginbidder'),
    path('register/', register , name='register'),
    path('login/', login , name='login'),
	path('registervendor/',VendorProfileRegister.as_view()),
	path('loginvendor/',Vendorlogin.as_view()),

]