# diamndPrject

The data is organized into an object containing seven arrays using the createDataArrayAll function, which takes in a csv filename as input. Once the createDataArrayAll function has been run (i.e. data = createDataArrayAll("latestSwing.csv"), each column of data can be accessed by calling data.[column name] (i.e. accelerationXcomponent = data.axs).

Then, the data would be extrapolated as follows: 
ax = data.axs
ay = data.ays
az = data.azs
wx = data.wxs
wy = data.wys
wz = data.wzs
time = data.time

Then, any of those seven values can be inputed in the data slot of the four specified functions:

for
searchContinuityAboveValue(data, start, end, thresh, winL),
#data# is one of the seven arrays created with createDataArrayAll
#start# and #end# are integer values corresponding to the beginning and ending indexes
#thresh# is an integer corresponding to the threshold specified for data
#winL# is an integer value corresponding to the number of samples in a row we check against the thresh predicate

for 
backSearchContinuityWithinRange(data, start, end, threshLo, threshHi, winL),
#data# is one of the sesven arrays created in the createDataArrayAll function
#start# and #end# are integer values corresponding to the beginning and ending indexes
#threshLo# is an integer value corresponding to the low end of the threshold
#threshHi# is an integer value corresponding to the high end of the threshold
#winL# is an integer value corresponding to the number of samples in a row we check against the thresh predicate

for
searchContinuityAboveValueTwoSignals(data1, data2, start, end, thresh1, thresh2, winL),
#data1# is an array created with createDataArrayAll
#data2# is an array created with createDataArrayAll
#start# and #end# are integer values corresponding to the beginning and ending indexes
#thresh1# is an integer corresponding to the threshold specified for data1
#thresh2# is an integer corresponding to the threshold specified for data2
#winL# is an integer value corresponding to the number of samples in a row we check against the thresh predicate

for
searchMultiContinuityWithinRange(data, start, end, threshLo, threshHi, winLength)
#data# is an array created with createDataArrayAll
#start# and #end# are integer values corresponding to the beginning and ending indexes
#threshLo# is an integer value corresponding to the low end of the threshold
#threshHi# is an integer value corresponding to the high end of the threshold
#winLength# is an integer value corresponding to the number of samples in a row we check against the thresh predicate

BONUS: I believe that impact occurs between timestamps 1218711 and 1233695, as I see the accelerations shift from increasing to decreasing or decreasing to increasing in that range.
