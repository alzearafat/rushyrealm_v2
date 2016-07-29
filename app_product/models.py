from __future__ import unicode_literals

import datetime
from decimal import Decimal
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

# MODEL ORM
class Product(models.Model):
  gambar          = models.ImageField(upload_to='images/%Y/%m/%d', blank=False, null=False)
  gambar_kecil_1  = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
  gambar_kecil_2  = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
  kategori        = models.ForeignKey('Product_Categories', on_delete=models.CASCADE)
  kode            = models.CharField(max_length=200, unique=True, blank=False, null=False)
  nama            = models.CharField(max_length=200, blank=False, null=False)
  harga           = models.IntegerField(blank=False, null=False)
  keterangan      = RichTextField(config_name='default', blank=False, null=False)
  sale            = models.BooleanField(default=False)
  sale_percent    = models.IntegerField(blank=True, null=True)
  tanggal_publish = models.DateField(default=datetime.datetime.now, null=True, blank=True)

  def _get_total_diskon(self):
    return self.sale_percent * self.harga / 100
  total_diskon = property(_get_total_diskon)

  def _get_total_harga_setelah_diskon(self):
    return self.harga - self.total_diskon
  total_harga_setelah_diskon = property(_get_total_harga_setelah_diskon)

  def __str__(self):
    return str(self.nama)


class Product_Categories(models.Model):
  id            = models.AutoField(primary_key=True)
  nama_kategori = models.CharField(max_length=200, blank=True, null=True)

  def __str__(self):
    return str(self.nama_kategori)
