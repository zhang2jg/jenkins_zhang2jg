# -*- coding:utf8 -*-
import base64
import requests
import json


def main(username, password, uaa_issuerID):
    # Request token
    encoded = base64.b64encode(username + ":" + password)
    headers = {'accept': r'application/json', 'authorization': 'Basic ' + encoded}
    data = {
        'client_id': username,
        'grant_type': 'client_credentials'}

    r = requests.post(uaa_issuerID, headers=headers, data=data)
    json_data = json.loads(r.text)
    token = str(json_data['access_token'])
    with open('predix_token.txt', 'w') as f:
        f.write(token)
    return token


if __name__ == '__main__':
    username = "jing_uaa_1"
    password = "A123"
    uaa_issuerID = r'https://7b70b04a-4402-4bdc-8fda-1ca7c6d94d25.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/token'
    print main(username, password, uaa_issuerID)
