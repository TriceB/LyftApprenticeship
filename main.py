"""
Lyft Apprenticeship application
Lyft Interview Test
Prompt
Please write a small web application in Python/Ruby/Node. The application only needs to do the following:

Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
Return a JSON object with the key “return_string” and a string containing every third letter from the original string.
Example
If you POST

{"string_to_cut": "iamyourlyftdriver"}
it will return:
{"return_string": "muydv"}
Note: To see expected behavior you can test against a current working example with the command:

curl -X POST https://lyft-interview-test.glitch.me/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
"""
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/test', methods=["POST"])
def get_string_to_cut():
	"""
	This will get the string that was submitted in the POST request and cut the string pulling out every 3rd letter
	of the string submitted.
	:return: a JSON object with the key "return_string" and the resulting value after cutting the string
	"""
	
	# if request.method == "POST":
	# get the string from the POST request submitted as JSON
	json_data = {"string_to_cut": request.json["string_to_cut"]}
	
	# cut the string from json_data to pull only every 3rd letter of the string submitted by using string slicing
	return_string = json_data["string_to_cut"][2::3]
	
	# print(return_string)
	
	# store the result of the slice in dict
	return_string_json = {"return_string": return_string}
	
	return return_string_json


if __name__ == '__main__':
	app.run(debug=True)
	app.jinja_env.auto_reload = True
	
	