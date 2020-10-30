from django.db import models
from django.contrib.auth.models import User


# Create your models here.

from core.models import DATEAbstractModel, CreateUpdateByAbstractModel, STATUSAbstractModel


class BidderProfile(DATEAbstractModel, CreateUpdateByAbstractModel, STATUSAbstractModel):

	first_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	isd = models.CharField(max_length=20)
	phone_no = models.CharField(max_length=20, verbose_name='Mobile No.')
	bidder_thumbnail = models.FileField(upload_to='vendor_profile_pic', null=True, blank=True)
	passwords = models.CharField(max_length =50)
	address = models.CharField(max_length=500, null=True, blank=True)
	is_profile_completed = models.BooleanField(default=False)
	auth_user = models.ForeignKey(
		User,
		related_name='bidder_profile_user',
		on_delete=models.CASCADE
	)

	class Meta:
		verbose_name = 'Bidder Profile'
		verbose_name_plural = 'Bidder Profile'
		db_table = 'bidder_profile'

	def __str__(self):

		return str(self.isd + self.phone_no)

