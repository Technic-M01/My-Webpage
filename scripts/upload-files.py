import boto3
import os
import time
import argparse
import json

BUCKET_NAME = "mauriciocodes.com"

session = None
s3 = None

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--credpath", type=str, required=True, help="path to aws credentials file")
parser.add_argument("-p", "--pushall", type=bool, help="skip confirmation prompt for files with changes and push everything")

args = parser.parse_args()


def listBucketObjects():
    my_bucket = s3.Bucket(BUCKET_NAME)

    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)

# TODO use both modification times, and file size when checking if file needs upload
def isModified(file_path: str, debugPrint = False):

    file_name = file_path.split("/")[-1]

    obj = s3.Object(BUCKET_NAME, file_name)

    file_modified = int(os.path.getmtime(file_path))
    file_size = os.stat(file_path)

    lm_to_local = obj.last_modified.astimezone() 
    object_modified = time.mktime(lm_to_local.timetuple())

    if debugPrint:
        print(f"obj modified: {object_modified}\nlocal file modified: {file_modified}\nobj lenght: {obj.content_length}(bytes)\nfile length: {file_size.st_size}(bytes)\nlocal file newer? {object_modified < file_modified}")

    return object_modified < file_modified

# path in s3. ex/ root/pages/resume/picture/newheadshot.jpg
def uploadFile(key, path):
    body = open(path, 'rb')

    s3.Bucket(BUCKET_NAME).put_object(
        Key = key,
        Body = body
    )

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
        modified = isModified(file_path)
        # print(f"file: {f} modified? {modified}\n")

        if modified and args.pushall != None:

            print(f"file: {f} has local changes. Push local changes to bucket: {BUCKET_NAME} ? (will overwrite existing file in bucket)")
            answer = input("[y/n]")

            if answer == "Y" or answer == "y":
                print(f"uploading file {f}")
                time.sleep(1)
                # uploadFile(f, file_path)
            else:
                print(f"Skipping upload of file {f}")
        elif modified:
            print(f"uploading file {f}")
            time.sleep(1)
            # uploadFile(f, file_path)

def readCredentials(file_path):
    access_key_id = ""
    secret_access_key = ""
    region = ""

    global session, s3

    file = open(file_path)
    data = json.load(file)
    
    credCount = 0

    for entry in data:
        if entry == "ACCESS_KEY_ID":
            access_key_id = data[entry]
            credCount += 1
        elif entry == "SECRET_ACCESS_KEY":
            secret_access_key = data[entry]
            credCount += 1
        elif entry == "REGION":
            region = data[entry]
            credCount += 1
        elif entry == "PROFILE_NAME":
            print(f"Retrieving credentials for profile: {data[entry]}")

    if credCount == 3:
        session = boto3.Session(region_name=region, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
        s3 = session.resource('s3')

        print("Credentials retrieved. Session set.")
    else:
        print(f"Error: not all necessary credentials were found in the given file, {file_path}")
        exit(0)


if __name__ == "__main__":

    credentials = args.credpath
    if os.path.exists(credentials):
        readCredentials(credentials)

        getWebpageFiles()
        # downloadFile("index.html", "new-index.html")