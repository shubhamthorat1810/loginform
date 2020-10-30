from django.db import models
from django.contrib.auth.models import User

# smart-select library

from core.models import DATEAbstractModel, CreateUpdateByAbstractModel, STATUSAbstractModel


class VendorProfile(DATEAbstractModel, CreateUpdateByAbstractModel, STATUSAbstractModel):

	first_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	isd = models.CharField(max_length=20)
	phone_no = models.CharField(max_length=20, verbose_name='Mobile No.')
	vendor_thumbnail = models.FileField(upload_to='vendor_profile_pic', null=True, blank=True)
	passwords = models.CharField(max_length =50)
	address = models.CharField(max_length=500, null=True, blank=True)
	is_profile_completed = models.BooleanField(default=False)
	auth_user = models.ForeignKey(
		User,
		related_name='vendor_profile_user',
		on_delete=models.CASCADE
	)

	class Meta:
		verbose_name = 'Vendor Profile'
		verbose_name_plural = 'Vendor Profile'
		db_table = 'vendor_profile'

	def __str__(self):

		return str(self.isd + self.phone_no)

