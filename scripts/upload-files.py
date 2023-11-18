import boto3
import os
import time

from datetime import datetime, timezone


REGION = "us-east-2"

BUCKET_NAME = "mauriciocodes.com"

session = boto3.Session(region_name=REGION, aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY_ID)

s3 = session.resource('s3')


def listBucketObjects():
    my_bucket = s3.Bucket(BUCKET_NAME)

    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)

def isModified():
    obj = s3.Object(BUCKET_NAME, 'index.html')

    file_modified = int(os.path.getmtime('/home/mauriciov/projects/My-Webpage/index.html'))

    file_size = os.stat('/home/mauriciov/projects/My-Webpage/index.html')

    # adjusting the 'last_modified' datetime to the local timezone
    lm_to_local = obj.last_modified.astimezone() 
    object_modified = time.mktime(lm_to_local.timetuple())

    print(f"obj modified: {object_modified}\nlocal file modified: {file_modified}\nobj lenght: {obj.content_length}(bytes)\nfile length: {file_size.st_size}(bytes)\nlocal file newer? {object_modified < file_modified}")

    return object_modified < file_modified

def uploadFile():
    # path in s3. ex/ root/pages/resume/picture/newheadshot.jpg
    key = 'test.txt'

    s3.Bucket(BUCKET_NAME).put_object(
        Key = key,
        Body = open('/home/mauriciov/projects/My-Webpage/test.txt', 'rb')
    )

def downloadFile():
    s3.Bucket(BUCKET_NAME).download_file('test.txt', 'test2.txt')


def getWebpageFiles():
    cwd = os.getcwd()

    parent = os.path.abspath(os.path.join(cwd, os.pardir))

    print(f"Current directory: {cwd}\nParent directory: {parent}")

    files = os.listdir(parent)
    print(f"files: {files}")

    # file_list = []

    # for (root, dirs, file) in os.walk(parent):
    #     for f in file:
    #         if '.jpg' in f:
    #             print(f)
    #         elif '.css' in f:
    #             print(f)
    #         elif '.js' in f:
    #             print(f)
    #         elif '.html' in f:
    #             print(f)


# modified = isModified()

# print(f"modified: {modified}")

# uploadFile()
downloadFile()