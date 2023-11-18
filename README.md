# Description 
Repository to hold the source code of my personal webpage and the uploading scripts used in development. 
AWS was used to hold the source code files, host the website, and handle website traffic.

# Implementation
A S3 bucket is setup for static website hosting, and contains the source code of the website.\
A hosted zone is created, and the name servers are added to the DNS of my domain. (done manually since I didn't register a domain with Route 53)\
A CloudFront distribution is setup with an SSL/TLS certificate, and points to the S3 buckets website endpoint.\
The record in the previously created hosted zone is configured to point to the new CloudFront distribution (originally pointing to the S3 buckets website endpoint)

# Additional Development
The webpage is currently setup to only show my resumé, but in the future I plan on adding pages to showcase some of the things I've worked on and created both personally and professionally.

## Planned Features

- [ ] adding pagination to view either just my resumé, or a page with my projects

- [ ] Better/more css for page styling

- [ ] More interactivity for the user

- [X] adding scripts to update source code files in the S3 bucket from the terminal. (currently replacing files and invalidating CloudFront distribution cache manually.)

## Python Scripts
### setup
inside the scripts directory, create a python3.8< virtual environment and install all the apt packages from requirements.txt

### Usage
The python script to upload locally modified source code to the S3 bucket **must** be run from inside the scripts directory.\
Providing the path to a json file that contains necessart AWS credentials is required to run the script and execute any actions on the cloud resources.

# Website
This was a quick, fun project to do so I can learn more AWS services hands on, and get the practice in for when I eventually take the Cloud Practicioner exam!\
If you're interested in seeing the website, here's the link: [mauriciocodes.com](https://mauriciocodes.com/)

Thanks for taking a look!
:) 
