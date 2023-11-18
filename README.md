# Description 
Repository to hold the source code of my personal webpage. 
AWS was used to hold the source code files, host the website, and handle website traffic.

# Implementation
A S3 bucket is setup for static website hosting, and contains the source code of the website.\
A hosted zone is created, and the name servers are added to the DNS of my domain. (done manually since I didn't register a domain with Route 53)\
A CloudFront distribution is setup with an SSL/TLS certificate, and points to the S3 buckets website endpoint.\
The record in the previously created hosted zone is configured to point to the new CloudFront distribution (originally pointing to the S3 buckets website endpoint)


#Website
This was a quick, fun project to do so I can learn more AWS services hands on, and get the practice in for when I eventually take the Cloud Practicioner exam!\
If you're interested in seeing the website, here's the link: [mauriciocodes.com](https://mauriciocodes.com/)

Thanks for taking a look!
:) 
