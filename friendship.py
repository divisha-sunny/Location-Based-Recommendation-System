import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import operator

def getFriendLocs(userid):
   
    df_gowalla_edges = pd.read_csv('data\loc-gowalla_edges.txt\Gowalla_edges.txt', sep='\t', header=None)
    df_gowalla_edges.columns = ['userid','friendship_links']
    #df_gowalla_edges

    df_gowalla = pd.read_csv('data\loc-gowalla_totalCheckins.txt\Gowalla_totalCheckins.txt', sep='\t', header=None)
    df_gowalla.columns = ['userid','timestamp','latitude','longitude','spotid']

    lon_min, lat_min, lon_max, lat_max = -74.2589, 40.4774, -73.7004, 40.9176
    nyc_events = df_gowalla[(df_gowalla['longitude']>lon_min) & 
            (df_gowalla['longitude']<lon_max) & 
            (df_gowalla['latitude']>lat_min) & 
            (df_gowalla['latitude']<lat_max)]
    venues = pd.read_csv('data\spots.txt\spots.txt', sep='\t', header=0)
    nyc_events = pd.DataFrame.merge(nyc_events, venues[['spotid','spotname']], on='spotid', how="inner")
    #nyc_events.head()
    
    locFreq = {}

    for friendId in df_gowalla_edges[df_gowalla_edges['userid']==userid]['friendship_links']: 
        friendLocs = nyc_events[nyc_events['userid']==friendId] 
        if not (friendLocs.empty): 
            for spotname in friendLocs['spotname']:
                if(locFreq.get(spotname) == None):
                    locFreq[spotname] = 1
                else: 
                    locFreq[spotname] = locFreq[spotname] + 1

    # locFreq = sorted(locFreq.items(), key=operator.itemgetter(1), reverse=True)[:5] 

    locFreqDf = pd.DataFrame(columns=['spotid', 'spotname', 'count'])

    for key, value in locFreq.items():
        spotid=nyc_events[nyc_events['spotname']==key]['spotid'].iloc[0]
        locFreqDf = locFreqDf.append({'spotid': spotid , 'spotname': key, 'count': value}, ignore_index=True)

    locFreqDf = locFreqDf.sort_values(by = 'count', ascending = False)
    return locFreqDf[:30]
