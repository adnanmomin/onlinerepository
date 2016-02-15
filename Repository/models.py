# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class RepositoryUploaddata(models.Model):
    file_name = models.CharField(max_length=40, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    upload_data = models.FileField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Repository_uploaddata'