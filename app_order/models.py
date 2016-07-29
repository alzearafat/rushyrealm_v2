from __future__ import unicode_literals

import uuid
import datetime
from django import forms
from django.db import models
from django.conf import settings
from django.forms import ModelForm

# MODEL ORM
class Order(models.Model):
  EXTRA2LARGE   = 'XXL'
  EXTRALARGE    = 'XL'
  LARGE         = 'L'
  MEDIUM        = 'M'
  SMALL         = 'S'
  SIZE_CHOICES  = (
    (EXTRA2LARGE, 'XXL'),
    (EXTRALARGE, 'XL'),
    (LARGE, 'L'),
    (MEDIUM, 'M'),
    (SMALL, 'S'),
  )
  id            = models.AutoField(primary_key=True, editable=False)
  kode_barang   = models.CharField(max_length=200, blank=False, null=False)
  ukuran        = models.CharField(max_length=3, choices=SIZE_CHOICES,)
  nama          = models.CharField(max_length=200, blank=False, null=False)
  email         = models.EmailField(max_length=200, blank=False, null=False)
  no_tlp        = models.CharField(max_length=200, blank=False, null=False)
  alamat        = models.TextField()
  tanggal_order = models.DateField(default=datetime.datetime.now, editable=False, null=True, blank=True)
  no_resi       = models.CharField(max_length=200, blank=False, null=False)
  lunas         = models.BooleanField(default=False)
  terkirim      = models.BooleanField(default=False)

  def __str__(self):
    return str(self.nama)

  def is_upperclass(self):
    return self.ukuran in (self.LARGE, self.MEDIUM)