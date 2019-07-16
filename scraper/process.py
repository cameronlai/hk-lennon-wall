# encoding=utf-8
# Input: JSON from scraper
# Output: CSV with lat long location information

import json
import pandas as pd
import subprocess
import sys
import re
import instaloader

# ---------------------
# config
# ---------------------
input_filename = 'data.json'
intermediate_filename = 'dataProcess.csv'
output_filename = 'data.csv'

# ---------------------
# global parameters
# ---------------------
pattern = re.compile("lat: ([0-9\.]+), lng: ([0-9\.]+)")
ig_loader = instaloader.Instaloader()

# ---------------------
# functions
# ---------------------
def get_latlong(location_name):
    try:
        cmd = 'instagram-scraper --search-location "{0}"'.format(location_name)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        print(p_status)
        print(output)
        loc_str = output.decode('utf-8').split('\r\n')[0]
        result = pattern.search(loc_str)
        print(result)
        ret = {}
        ret['lat'] = result.group(1)
        ret['lng'] = result.group(2)
        return ret
    except Exception as e:
        print(e)
        return None

def get_profile_username(user_id):
    try:
        profile = instaloader.Profile.from_id(ig_loader.context, int(user_id))    
        ret = {}
        ret['username'] = profile.username
        ret['full_name'] = profile.full_name
        return ret
    except Exception as e:
        print(e)
        return None

# ---------------------
# load data
# ---------------------
with open(input_filename, 'rb') as f:
    data = json.load(f)

df = pd.read_json(json.dumps(data['GraphImages']))
print(df.shape)

df = df.dropna(subset=['location'])
print(df.shape)

# ---------------------
# output data
# ---------------------
output_ary = []
for index, row in df.iterrows():   
    output_ary.append({
        'shortCode': row['shortcode'],
        'location':  row['location']['name'],
        'photoUrl': row['thumbnail_src'],
        'userId': row['owner']['id'],
        'latlng': [1.0, 1.0],
        'username': '-',
        'full_name': '-'
    })

# Fill in location
final_df = pd.DataFrame(output_ary)

location_dict = {}
for index, item in enumerate(final_df['location'].unique()):
    print('--')
    print(index)    
    ret = get_latlong(item)
    if ret != None:
        location_dict[item] = [ret['lat'], ret['lng']]

username_dict = {}
full_name_dict = {}
for index, item in enumerate(final_df['userId'].unique()):
    print('--')
    print(index)
    ret = get_profile_username(item)
    if ret != None:
        username_dict[item] = ret['username']
        full_name_dict[item] = ret['full_name']

for index, row in final_df.iterrows():
    print('--')
    print(index)
    final_df.loc[index]['latlng'] = location_dict[row['location']]
    final_df.loc[index]['username'] = username_dict[row['userId']]
    final_df.loc[index]['full_name'] = full_name_dict[row['userId']]

# Output to file
final_df.to_csv(output_filename, index=False)
print(final_df.head())