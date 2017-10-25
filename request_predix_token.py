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
    # TODO set username and password as environment variables in Jenkins environment
    username = "jing_uaa_1"
    password = ""
    uaa_issuerID = r''
    print main(username, password, uaa_issuerID)
