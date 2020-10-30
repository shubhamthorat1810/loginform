from rest_framework import serializers

from vendor.models import VendorProfile


class VendorProfileSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = VendorProfile
		fields = "__all__"
