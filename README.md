#Lyft Interview Test
*This is a submission for the Software Engineering Apprenticeship (2022)*

---
##Description
This is a web application that will cut a string by pulling out every 3rd letter in the string submitted.
It accepts a POST request using the argument "string_to_cut" where the user will fill in the string they would like to be cut.
The program will return a JSON object with the key "return_string" and a value with resulting string.

To test this out, you may run the code below by either running the Curl command, running the Python code below or by using Postman (instruction below).

###Curl
`curl --location --request POST 'https://lyftsweapprenticeship.herokuapp.com/test' --header 'Content-Type: application/json' --data-raw '{"string_to_cut": "iamyourlyftdriver"}'`

###Python
```
import requests


headers = {"Content-Type": "application/json"}

json_data = {"string_to_cut": "tryingthisthingoutitsatest"}

r = requests.post('https://lyftsweapprenticeship.herokuapp.com/test', headers=headers, json=json_data)
print(r.text)
```

###Postman
1. Add a new request tab
2. Change the Request type to "POST" in the dropdown
3. Enter the URL <https://lyftsweapprenticeship.herokuapp.com/test>
4. Choose the "Body" tab
5. Select the "raw" option
6. In the dropdown that appears to the right, choose "JSON"
7. In the text field type out the JSON object in the following format `{"string_to_cut": "iamyourlyftdriver"}`
8. Change the "iamyourlyftdriver" text to any string you wish to see cut
9. You will then see the results in the bottom panel


###Thank you for your time and consideration.