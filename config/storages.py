from storages.backends.s3boto3 import S3Boto3Storage 
from decouple import config

AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")


class StaticRootS3Boto3Storage(S3Boto3Storage):
    default_acl = "public-read"
    custom_domain = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
    location = "static/"

    # @property  # not cached like in parent of S3Boto3Storage class
    # def location(self):
    #     _location = parse_tenant_config_path('static/'+'%s')  # here you can just put '%s'
    #     return _location


class MediaRootS3Boto3Storage(S3Boto3Storage):
    file_overwrite = False
    default_acl = "public-read"
    custom_domain = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
    location = "media/"

    # @property  # not cached like in parent of S3Boto3Storage class
    # def location(self):
    #     _location = parse_tenant_config_path(
    #         "media/" + "%s"
    #     )  # here you can just put '%s'
    #     return _location
