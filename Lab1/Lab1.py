import requests
# virtualenv

# print(requests.__version__)

# curl
# response = requests.get('http://google.com')
# print(response)

# Print source code
rawURL = 'https://raw.githubusercontent.com/JohnDoeMask/CMPUT404Labs/master/Lab1/Lab1.py'
response = requests.get(rawURL)
print(response.text)
