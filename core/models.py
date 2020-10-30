from django.db import models
from django.contrib.auth.models import User

# smart-select library
from django.core.validators import MaxValueValidator, MinValueValidator




class DATEAbstractModel(models.Model):
    """
    created at and updated at fields
    abstract models
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    # objects=models.Manager()

    class Meta:
        """
        class container with some options attached to the model
        """
        abstract = True


class CreateUpdateByAbstractModel(models.Model):
    """
    created updated by abstract model
    """
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='created_%(class)ss',
        verbose_name='Created By',
        limit_choices_to=~models.Q(is_staff=0, is_superuser=0),
        db_column='created_by',
        blank=True, null=True
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='updated_%(class)ss',
        verbose_name='Updated By',
        limit_choices_to=~models.Q(is_staff=0, is_superuser=0),
        db_column='updated_by',
        blank=True, null=True
    )
    # objects=models.Manager()

    class Meta:
        """
        class container with some options attached to the model
        """
        abstract = True


class STATUSAbstractModel(models.Model):
    """
    status abstract model
    """
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    # objects=models.Manager()

    class Meta:
        """
        class container with some options attached to the model
        """
        abstract = True


