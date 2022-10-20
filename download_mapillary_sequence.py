#####################  Scripts for downloading multicamera benchmarks in Mapilllary API v4.0 ########################
import mapillary as mly
from mapillary.models.geojson import GeoJSON
import json
import os, glob, requests
from os.path import exists

# Output directory
out_path = ' '

# Mapillary access token -- user should provide their own
access_token = 'MLY|'

#Request access to mapillary
mly.interface.set_access_token(access_token)


# Read merged json_file
f = open('{sequence_id}.geojson')
data = json.load(f)


if not os.path.exists(out_path):
    os.makedirs(out_path)
    os.makedirs(out_path+"/rgb")

print('Saving Mapillary imagery...')
 create a folder for each unique sequence ID to group images by sequence
for i, feature in enumerate(data['features']):
    sequence_id = feature['properties']['sequence_id']
    if not os.path.exists(out_path+"/tmp/"+sequence_id):
        os.makedirs(out_path+"/tmp/"+sequence_id)

    # get lng,lat of each feature
    LON = feature['geometry']['coordinates'][0]
    LAT = feature['geometry']['coordinates'][1]
        
    # request the URL of each image
    image_id = feature['properties']['id']
    header = {'Authorization' : 'OAuth {}'.format(access_token)}
    #url = 'https://graph.mapillary.com/{}?fields=thumb_256_url'.format(image_id)
    url = 'https://graph.mapillary.com/{}?fields=thumb_original_url'.format(image_id)
    r = requests.get(url, headers=header)
    data = r.json()
    #image_url = data['thumb_256_url'] #256,1024,2048,original
    image_url = data['thumb_original_url']

    # save each image with ID as filename to directory by sequence ID
    if i%n==0:
        with open(f'{out_path}/tmp/{sequence_id}/{i:06}.jpg', 'wb') as handler:
            image_data = requests.get(image_url, stream=True).content
            handler.write(image_data)     

sys_stream = "mv "+out_path+"/tmp/**/*.jpg "+out_path+"/rgb"
os.system(sys_stream)

print('DONE!')
