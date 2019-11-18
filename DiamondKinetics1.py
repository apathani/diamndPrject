import csv
import unittest


class SwingData(object):
    def __init__(self,time,ax,ay,az,wx,wy,wz):
        self.time = time
        self.axs = ax
        self.ays = ay
        self.azs = az
        self.wxs = wx
        self.wys = wy
        self.wzs = wz

    def Greater (self,other):
        if self.axs > other.axs and self.ays > other.ays and self.axs > other.axs:
            return self.wxs > other.wxs and self.wys > other.wys and self.wzs > other.wzs
        else:
            return False


    def Less (self,other):
        if self.axs < other.axs and self.ays < other.ays and self.axs < other.axs:
            return self.wxs < other.wxs and self.wys < other.wys and self.wzs < other.wzs
        else:
            return False



#extrapolate data from csv file, returns allData, a SwingData object comprised
#of seven data arrays corresponding to time, ax, ay, az, wx, wy, wz.
def createDataArrayAll(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file)
        allData = []
        for row in csv_reader:
            new = SwingData(float(row[0]),float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]))
            allData =  allData + [new]
        return allData


#data is an array of swingData objects created with createDataArrayAll

#start and end are real number values corresponding to the beginning and ending indexes

#threshLo, if less than threshHi, is the lower bound of a search to find within range. Otherwise it is the top bound search out
#of range. If there are two data streams, (two swings) it is the threshold for the first data stream.

#threshHi, if less than threshLo, is the lower bound of a search to find out of range values. Otherwise it is the top bound for a search within range. If there are two data streams, (two swings) it is the threshold for the second data stream.

#winL is an real number value corresponding to the number of samples in a row we check against the thresh predicate

def continuityHelper(data,data2,start,end,threshLo, threshHi, winL):
    count = 0
    if (data2==[]):
        if threshLo.Less(threshHi):
            for i in range(start,end):
                if (data[i].Greater(threshLo) and data[i].Less(threshHi)):
                    count += 1
                else:
                    count = 0
                if count == winL:
                    return i-winL+1
        else:
            for i in range(start,end):
                if (threshHi.Greater(data[i]) or threshLo.Less(data[i])):
                    count += 1
                else:
                    count = 0
                if count == winL:
                    return i-winL+1
        return None
    else:
        for i in range(start,end):
            if data[i].Greater(threshLo) and data2[i].Greater(threshHi):
                count += 1
            else:
                count = 0
            if count == winL:
                return i-winL+1
        return None
    return None

#data is one of the seven arrays created in the createDataArrayAll function

#start and end are real number values corresponding to the beginning and ending indexes

#threshLo is a swingData object representing the threshLo. If the threshLo is above the threshHi, the function will search outside of the range.

#winL is an real number value corresponding to the number of samples in a row we check against the thresh predicate

def searchContinuityAboveValue(data, start, end, thresh, winL):
    return continuityHelper(data,[],start,end,thresh,SwingData(float(999999),float(999999),
        float(999999),float(999999),float(999999),float(999999),float(999999)), winL)


#data is one of the seven arrays created in the createDataArrayAll function

#start and end are real number values corresponding to the beginning and ending indexes

#threshLo is a swingData object representing the threshLo. If the threshLo is above the threshHi, the function will search outside of the range.

#threshHi is a swingData object representing the threshHi. If the threshHi is above the threshLo, the function will search within the range.

#winL is an real number value corresponding to the number of samples in a row we check against the thresh predicate



def backSearchContinuityWithinRange(data, start, end, threshLo, threshHi, winL):
    return continuityHelper(data,[],start,end,threshLo,threshHi,winL)



#data1 is one of seven arrays created with createDataArrayAll
#data2 is one of seven arrays created with createDataArrayAll

#start and end are real number values corresponding to the beginning and ending indexes

#thresh1 is a swingData object representing the threshold for the first data stream.

#thresh2 is a swingData object representing the threshold for the second data stream.

#winL is an real number value corresponding to the number of samples in a row we check against the thresh predicate

def searchContinuityAboveValueTwoSignals(data1, data2, start, end, thresh1, thresh2, winL):
    return continuityHelper(data1, data2, start, end, thresh1,thresh2,winL)


#data is an array created with createDataArrayAll

#start and end are real number values corresponding to the beginning and ending indexes

#threshLo is a swingData object representing the threshLo. If the threshLo is above the threshHi, the function will search outside of the range.

#threshHi is a swingData object representing the threshHi. If the threshHi is above the threshLo, the function will search within the range

#winL is an real number value corresponding to the number of samples in a row we check against the thresh predicates

###IMPORTANT : : : threshHi and threshLo must have matching boolean values : : : IMPORTANT#######

def searchMultiContinuityWithinRange(data, start, end, threshLo, threshHi, winLength):
    if start == end:
        return []
    else:
        i = backSearchContinuityWithinRange(data, start, end, threshLo, threshHi, winLength)
        if i == None:
            return []
        else:
            return [(i,i+winLength-1)] + searchMultiContinuityWithinRange(data, i + winLength, end, threshLo,threshHi,winLength)



