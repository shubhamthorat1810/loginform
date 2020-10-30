from rest_framework import serializers

from bidder.models import BidderProfile


class BidderProfileSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = BidderProfile
		fields = "__all__"
