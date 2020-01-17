import requests

parameters = {
    "op"
}

response = requests.post('https://IPFIREWALL/api/?', params=parameters)

if response:
    print('Request is successful.')
    print(response)
else:
    print('Request returned an error.')
