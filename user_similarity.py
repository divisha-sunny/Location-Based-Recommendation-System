import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

def prepareData():
    nyc_events = pd.read_csv('dataframes\\nyc_events_with_name.csv')
    nyc_events_clean = pd.read_csv('dataframes\\nyc_events_clean.csv')
    Ratings = pd.read_csv('dataframes\\Ratings.csv')
    Rating_avg = pd.read_csv('dataframes\\Rating_avg.csv')

    return nyc_events, nyc_events_clean, Ratings, Rating_avg

# def parse_datetime(s):
#     tzone = tz.timezone("America/New_York") #parse_datetime
#     utc = datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ')
#     return tz.utc.localize(utc).astimezone(tzone)

# def find_n_neighbours(df,n):
#     order = np.argsort(df.values, axis=1)[:, :n]
#     df = df.apply(lambda x: pd.Series(x.sort_values(ascending=False)
#            .iloc[:n].index, 
#           index=['top{}'.format(i) for i in range(1, n+1)]), axis=1)
#     return df   

# def get_similar_locations(user1, user2, Rating_avg):
#     common_locations = Rating_avg[Rating_avg.userId == user1].merge(
#         Rating_avg[Rating_avg.userId == user2],
#         on = "spotid",
#         how ="inner"
#     )
#     return common_locations.merge(nyc_events_clean, on = 'spotid')     

# def User_item_score(user,item):
#     final=pd.pivot_table(Rating_avg,values='adg_rating',index='userId',columns='spotid')
#     final_location = final.fillna(final.mean(axis=0))
#     final_user = final.apply(lambda row: row.fillna(row.mean()), axis=1)
#     cosine = cosine_similarity(final_location)
#     similarity_with_movie = pd.DataFrame(cosine,index=final_location.index)
#     similarity_with_movie.columns=final_user.index
#     sim_user_30_m = find_n_neighbours(similarity_with_movie,30)

#     a = sim_user_30_m[sim_user_30_m.index==user].values
#     b = a.squeeze().tolist()
#     c = final_location.loc[:,item]
#     d = c[c.index.isin(b)]
#     f = d[d.notnull()]
#     avg_user = Mean.loc[Mean['userId'] == user,'rating'].values[0]
#     index = f.index.values.squeeze().tolist()
#     corr = similarity_with_movie.loc[user,index]
#     fin = pd.concat([f, corr], axis=1)
#     fin.columns = ['adg_score','correlation']
#     fin['score']=fin.apply(lambda x:x['adg_score'] * x['correlation'],axis=1)
#     nume = fin['score'].sum()
#     deno = fin['correlation'].sum()
#     final_score = avg_user + (nume/deno)
#     return final_score 


# def User_item_score1(user, nyc_events, nyc_events_clean, Ratings, Rating_avg):
#     final=pd.pivot_table(Rating_avg,values='adg_rating',index='userId',columns='spotid')
#     final_location = final.fillna(final.mean(axis=0))
#     final_user = final.apply(lambda row: row.fillna(row.mean()), axis=1)
#     cosine = cosine_similarity(final_location)
#     similarity_with_movie = pd.DataFrame(cosine,index=final_location.index)
#     similarity_with_movie.columns=final_user.index
#     check = pd.pivot_table(Rating_avg,values='rating_x',index='userId',columns='spotid')
#     sim_user_30_m = find_n_neighbours(similarity_with_movie,30)
#     Location_user = Rating_avg.groupby(by = 'userId')['spotid'].apply(lambda x:','.join(x))

#     Locations_seen_by_user = check.columns[check[check.index==user].notna().any()].tolist()
#     a = sim_user_30_m[sim_user_30_m.index==user].values
#     b = a.squeeze().tolist()
#     d = Location_user[Location_user.index.isin(b)]
#     l = ','.join(d.values)
#     Locations_seen_by_similar_users = l.split(',')
#     Locations_under_consideration = list(set(Locations_seen_by_similar_users)-set(list(map(str, Locations_seen_by_user))))
#     Locations_under_consideration = list(map(int, Locations_under_consideration))
#     score = []

#     for item in Locations_under_consideration:
#         c = final_location.loc[:,item]
#         d = c[c.index.isin(b)]
#         f = d[d.notnull()]
#         avg_user = Mean.loc[Mean['userId'] == user,'rating'].values[0]
#         index = f.index.values.squeeze().tolist()
#         corr = similarity_with_movie.loc[user,index]
#         fin = pd.concat([f, corr], axis=1)
#         fin.columns = ['adg_score','correlation']
#         fin['score']=fin.apply(lambda x:x['adg_score'] * x['correlation'],axis=1)
#         nume = fin['score'].sum()
#         deno = fin['correlation'].sum()
#         final_score = avg_user + (nume/deno)
#         score.append(final_score)
#     data = pd.DataFrame({'spotid':Locations_under_consideration,'score':score})
#     top_30_recommendation = data.sort_values(by='score',ascending=False).head(30)
#     Location_Name = top_30_recommendation.merge(nyc_events_clean, how='inner', on='spotid')
#     Location_Names = Location_Name.spotname.values.tolist()
#     return Location_Names      

def getSimilarUserLocs():
   
    # nyc_events, nyc_events_clean, Ratings, Rating_avg = prepareData()

    # Rating_avg = Rating_avg.astype({"spotid": str})
    # Location_user = Rating_avg.groupby(by = 'userId')['spotid'].apply(lambda x:','.join(x))

    # #user = int(input("Enter the user id to whom you want to recommend : "))
    # predicted_locs = User_item_score1(9050, nyc_events, nyc_events_clean, Ratings, Rating_avg)
    # #print(" ")
    # #print("The Recommendations for User Id : "+user)
    # #print("   ")
    # # for i in predicted_movies:
    # #     print(i)
    # locFreqDf = pd.DataFrame(columns=['spotid', 'spotname'])

    # for spotname in predicted_locs:
    #     spotid=nyc_events[nyc_events['spotname']==spotname]['spotid'].iloc[0]
    #     locFreqDf = locFreqDf.append({'spotid': spotid , 'spotname': spotname}, ignore_index=True)

    collabDf = pd.read_csv('dataframes/collabDf.csv')
    
    return collabDf













