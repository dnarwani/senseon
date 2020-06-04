# Senseon Test 

### Check Internet Connection 

Run `check_internet_conn.py` to check the status of your internet connection. This script will check the following: 

a) Run a DNS nameserver query to 8.8.8.8 

b) Make sure you can send an HTTP request to any URL 

### Nginx Configuration 

In this script we configured 2 servers listening on port `5123` and `5124`. 

a) An app running on port 5123 will send a request to authenticate using API `/sso/auth`. 

b) This API currently sets up a basic auth with NGINX.

c) Once the credentials are verified, the app will redirect to the home page on port `5123`. 

d) If the verification fails, then a `401` page is displayed 

