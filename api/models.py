from django.db import models

class Play (models.Model)
title = models.CharField(max_length=250)
author = models.CharField(max_length=250)
pub_place = models.CharField(max_length=250)
pub_year = models.IntegerField(max_length=4)
pub_date = models.CharField(max_length=250)
publisher = models.CharField(max_length=250)
editor1 = models.CharField(max_length=250)
editor2 = models.CharField(max_length=250)
editor3 = models.CharField(max_length=250)
edition_num = models.IntegerField(max_length=4)
edition_name = models.CharField(max_length=250)

class Quote (models.Model)
word = models.CharField(max_length=250)
word_id = models.CharField(max_length=250)
quote = models.textField
act = models.IntegerField(max_length=4)
scene = models.IntegerField(max_length=4)
line = models.IntegerField(max_length=4)
line_id = models.CharField(max_length=250)
quote_type = models.IntegerField(max_length=4)
notes = models.textField

class Place_Real (models.Model)
name_mod = models.CharField(max_length=250)
name_alt = models.CharField(max_length=250)
lat = 
long =
poly = 
notes = models.textField
place_type = models.CharField(max_length=250)

class Place_Fictional (models.Model)
Name_Standard = models.CharField(max_length=250)
Name_Alt = models.CharField(max_length=250)
Notes = models.textField

class Place_Historical (models.Model)
name_hist = models.CharField(max_length=250)
name_alt = models.CharField(max_length=250)
lat = 
long =
poly = 
notes = models.textField
place_type = models.CharField(max_length=250)

class Image (models.Model):
image_file_name = models.CharField(max_length=250)
image_file_size = models.CharField(max_length=250)
image_id = models.CharField(max_length=250)
image_ext = models.CharField(max_length=250)