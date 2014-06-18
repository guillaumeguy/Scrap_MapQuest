import urllib2
import json

key_path = 

with open(key_path, 'r') as key_file:
   key = key_file.read() ## API key to get from website


org_lon = [3.150000095,3.150000095]
org_lat = [47,48]
dst_lat = [[50.216667,46.1,45.2],[43.216667,47.1]]
dst_lon = [[3.5,4.2,3.5],[3.8,4.2]]

base_url = 'http://www.mapquestapi.com/directions/v2/routematrix?key=%s&locations&json={"locations":[' %key

def build_url(lon,lat):
    url = '{"latLng":{"lng":%s,"lat":%s}}' %(lon,lat)
    return url

def recursive_build_line(lon_list,lat_list):
    if len(lon_list)==1:
        return build_url(lon_list[0],lat_list[0])
    return build_url(lon_list[0],lat_list[0]) + ',' + recursive_build_line(lon_list[1:],lat_list[1:])

#f = open('travel_matrix.csv', 'wb')
#data = csv.writer(f)

for org_lat_it,org_lon_it,dst_lon_it,dst_lat_it in zip(org_lat,org_lon,dst_lon,dst_lat):
        
    address = base_url + build_url(org_lon_it,org_lat_it) + ',' + recursive_build_line(dst_lon_it,dst_lat_it) + ']}]}'   
    print address
    json_return  = json.loads(urllib2.urlopen(address).read())
    print json_return['time']
    print json_return['distance']

#f.close()


