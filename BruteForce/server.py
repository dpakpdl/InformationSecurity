from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
	post_payload = request.form
	username = post_payload.get('username')
	password = post_payload.get('password')
	if username == 'Deepak' and password == '1994':
		return jsonify({'message': 'Login Successful', 'success': True})
	return jsonify({'message': 'Login failed', 'success': False})


app.run(debug=True)