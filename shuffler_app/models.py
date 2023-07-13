# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)

	# class Meta:
	# 	db_table = 'players'

# Create your models here.
