from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


# To have static content in one directory in S3
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


# To have media content in another directory in S3
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
