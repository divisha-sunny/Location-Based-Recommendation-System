import operator
import numpy as np

from friendship import getFriendLocs
from user_similarity import getSimilarUserLocs
from locations import getnearbyLocs, getNearbyTopLocs

# it has all locations recommended based on users which have similar history as the current user
# recommending based on user similarity, just say this
collabDf = getSimilarUserLocs()
# print(collabDf)
# print("\n---------------------------------")

nearbyLocs = getnearbyLocs(-74, 40.55)
# print(nearbyLocs)
# print("\n---------------------------------")
#the top location near us
#more importance to this location as it is top and nearby tell that also
nearbyTopLocs = getNearbyTopLocs(-74, 40.55) #don't iterate here, only one na ok? it is harcoded for now, you can tell some python issue was there, so couldn't
# print(nearbyTopLocs)
# print("\n---------------------------------")

friendLocs = getFriendLocs(320)
# print(friendLocs)
# print("\n---------------------------------")

# have one dict
# iterate through all rows
# update dict
# sort it
# you will merge now

merge = {}
for spotname in collabDf['spotname']:
    if(merge.get(spotname)== None):
        merge[spotname]=1
    else:
        merge[spotname]=merge[spotname]+1

for spotname in nearbyLocs:
    if(merge.get(spotname)== None):
        merge[spotname]=1
    else:
        merge[spotname]=merge[spotname]+1

for spotname in friendLocs['spotname']:
    if(merge.get(spotname)== None):
        merge[spotname]=1
    else:
        merge[spotname]=merge[spotname]+1      

merge =  sorted(merge.items(), key=operator.itemgetter(1), reverse=True)

recommended =  nearbyTopLocs

for entry in merge[:10]:
    #print(entry[0])
    recommended = np.append(recommended, entry[0])

print(recommended)
# no intersection between these 3 lists
# let's think

