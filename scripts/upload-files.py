import boto3
import os
import time


REGION = "us-east-2"

BUCKET_NAME = "mauriciocodes.com"

session = boto3.Session(region_name=REGION, aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY_ID)

s3 = session.resource('s3')


def listBucketObjects():
    my_bucket = s3.Bucket(BUCKET_NAME)

    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)

# TODO use both modification times, and file size when checking if file needs upload
def isModified(file_path: str, debugPrint = False):

    file_name = file_path.split("/")[-1]

    # obj = s3.Object(BUCKET_NAME, 'index.html')
    obj = s3.Object(BUCKET_NAME, file_name)

    # file_modified = int(os.path.getmtime('/home/mauriciov/projects/My-Webpage/index.html'))
    file_modified = int(os.path.getmtime(file_path))

    # file_size = os.stat('/home/mauriciov/projects/My-Webpage/index.html')
    file_size = os.stat(file_path)

    # adjusting the 'last_modified' datetime to the local timezone
    lm_to_local = obj.last_modified.astimezone() 
    object_modified = time.mktime(lm_to_local.timetuple())

    if debugPrint:
        print(f"obj modified: {object_modified}\nlocal file modified: {file_modified}\nobj lenght: {obj.content_length}(bytes)\nfile length: {file_size.st_size}(bytes)\nlocal file newer? {object_modified < file_modified}")

    return object_modified < file_modified

def uploadFile(key, path):
    # path in s3. ex/ root/pages/resume/picture/newheadshot.jpg
    # key = 'test.txt'

    body = open(path, 'rb')

    s3.Bucket(BUCKET_NAME).put_object(
        Key = key,
        Body = body
    )
        # Body = open('/home/mauriciov/projects/My-Webpage/test.txt', 'rb')


def downloadFile(file_name, download_file_name):
    s3.Bucket(BUCKET_NAME).download_file(file_name, download_file_name)

#TODO add a user prompt to confirm upload of file 
def getWebpageFiles():
    cwd = os.getcwd()

    parent = os.path.abspath(os.path.join(cwd, os.pardir))

    print(f"Current directory: {cwd}\nParent directory: {parent}")

    dir_path = os.path.abspath(os.path.join(parent, "webpage"))

    files = os.listdir(dir_path)
    print(f"files: {files}")

    for f in files:
        file_path = os.path.abspath(os.path.join(dir_path, f))
        modified = isModified(file_path, True)
        print(f"file: {f} modified? {modified}\n")

        if modified:
            # uploadFile(f, file_path)            
            print(f"file: {f}\npath: {file_path}")

# print(f"modified: {isModified('/home/mauriciov/projects/My-Webpage/index.html')}")

# getWebpageFiles()

# uploadFile()
# downloadFile("index.html", "new-index.html")