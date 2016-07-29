from __future__ import unicode_literals

import datetime
from django import forms
from django.db import models
from django.conf import settings
from django.forms import ModelForm
from django.core.exceptions import ValidationError

# CUSTOM FILE SIZE VALIDATOR
def validate_image(fieldfile_obj):
    filesize        = fieldfile_obj.file.size
    megabyte_limit  = 1.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

# MODEL ORM
class Confirmation(models.Model):
  id_order            = models.CharField(max_length=200, blank=False, null=False)
  nama                = models.CharField(max_length=200, blank=False, null=False)
  jumlah_transfer     = models.CharField(max_length=200, blank=False, null=False)
  tanggal_transfer    = models.DateField(default=datetime.datetime.now, null=False, blank=False)
  tanggal_konfirmasi  = models.DateField(default=datetime.datetime.now, editable=False, null=True, blank=True)
  bukti_transfer      = models.ImageField(upload_to='images/%Y/%m/%d',  validators=[validate_image], blank=True, null=True)

  def __str__(self):
    return str(self.id_order)
