# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:26:48 2020

@author: Lara
"""
from pathlib import Path
import json
from pandas.io.json import json_normalize
import requests


def all_restaurants(query):
    api_key = Path("yelp_api_key.txt").read_text().strip()
    header = {'Authorization': 'Bearer %s' % api_key}
    url='https://api.yelp.com/v3/businesses/search?'
    param = {'location':query,'categories':'restaurants'}
    response=json.loads(requests.get(url, params=param, headers=header).content)
#    total=response['total']
    all_restaurant= json_normalize(response['businesses'])
    '''
    for i in range((int)(total/20)+1):
       # param = {'location':query,'categories':'restaurants','limit': 20,'offset': i*20}
       # response=json.loads(requests.get(url, params=param, headers=header).content)
        if 'businesses' in response:
            for j in range(len(response['businesses'])):
                all_restaurant.append(response['businesses'][j])
       # time.sleep(.300)
       '''
    return all_restaurant



#https://www.yelp.com/developers/documentation/v3

#https://devdocs.io/python~3.7/
    





def reviews(restaurant_id):
    api_key = Path("yelp_api_key.txt").read_text().strip()
    header = {'Authorization': 'Bearer %s' % api_key}
    url='https://api.yelp.com/v3/businesses/' + str(restaurant_id) + '/reviews'
    response=json.loads(requests.get(url,  headers=header).content)
    print(response)
    
    #example id: 'ra6Ejpr6Y5nJL1Um6pzTdg'