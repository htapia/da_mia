# haversine function to get distance

from math import * 
 
def haversine(lon1, lat1, lon2, lat2):
    """     
    Calculate the great circle distance between two points      
    on the earth (specified in decimal degrees)     
    """     
    # convert decimal degrees to radians      
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])     
    # haversine formula      
    dlon = lon2 - lon1      
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2     
    c = 2 * atan2(sqrt(a), sqrt(1-a))      
    km = 6367 * c    
    return km  