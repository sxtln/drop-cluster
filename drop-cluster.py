import argparse
import http.client
import json
import time
import os


parser = argparse.ArgumentParser()

parser.add_argument('--cluster-id', help='id of the cluster to drop',required=True)
parser.add_argument('--apikey',required=True)


args = parser.parse_args()


req_headers = {'Authorization': f'Bearer {args.apikey}'}
try:
    print(f'starting to dropped cluster {args.cluster_id}')
    conn = http.client.HTTPSConnection('api.sextillion.io')
    conn.request('DELETE', f'/sc/cluster/{args.cluster_id}',headers=req_headers)
    hres = conn.getresponse()
    if hres.status != 200:
        print(f'failed to delete cluster {hres.reason}')
        exit(1)
    print(f'successfully dropped cluster {args.cluster_id}')
    
except Exception as ex:
    print('failed to delete cluster', ex)
    exit(1)
