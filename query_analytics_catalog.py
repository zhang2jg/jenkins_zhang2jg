# -*- coding:utf8 -*-

import base64
import requests
import json
import os


def main(uri, predix_zone_id, predix_token):
    # Request token
    headers = {'content-type': r'application/json',
               'authorization': 'Bearer ' + predix_token,
               'predix-zone-id': predix_zone_id}

    r = requests.get(uri, headers=headers)
    json_data = json.loads(r.text)
    analytics_catalog = str(json_data['analyticCatalogEntries'])
    return analytics_catalog


if __name__ == '__main__':
    # TODO set username and password as environment variables in Jenkins environment
    predix_analytics_uri = r'https://predix-analytics-catalog-release.run.aws-usw02-pr.ice.predix.io/api/v1/catalog/analytics'
    predix_zone_id = r''
    with open('predix_token.txt', 'r') as f:
        predix_token = f.read()
    print main(predix_analytics_uri, predix_zone_id, predix_token)