import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import pytz as tz
from datetime import datetime
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pickle


def parse_datetime(s):
    tzone = tz.timezone("America/New_York") #parse_datetime
    utc = datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ')
    return tz.utc.localize(utc).astimezone(tzone)

def recommend_venues(df, longitude, latitude):
    kmeans = pickle.load(open('models/kmeans.pkl', 'rb'))
    predicted_cluster = kmeans.predict(np.array([longitude,latitude]).reshape(1,-1))[0]
    # Fetch the venue name of the top most record in the topvenues dataframe for the predicted cluster
    venue_name = df[df['cluster']==predicted_cluster]['spotname']
    return venue_name.unique()

def prepareData():
    nyc_events = pd.read_csv('dataframes\\nyc_events.csv')
    return nyc_events

#return a list of spotnames
def getNearbyTopLocs(lat, lng): 
    topvenues_df = pd.read_csv('dataframes\\topvenues_df.csv')
    return recommend_venues(topvenues_df, lat, lng)

#return a list of spotnames
def getnearbyLocs(lat, lng):
    nyc_events = prepareData()    
    return recommend_venues(nyc_events, lat, lng)
