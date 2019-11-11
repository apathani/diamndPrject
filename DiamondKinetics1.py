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
            new = SwingData(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            allData = [new] + allData
        return allData


#data is an array of swingData objects created with createDataArrayAll

#start and end are real number values corresponding to the beginning and ending indexes

#thresh is a swingData object with a boolean value for time that is true if searching above threshold and false if searching below.

#winL is an real number value corresponding to the number of samples in a row we check against the thresh predicate


def searchContinuityAboveValue(data, start, end, thresh, winL):
    count = 0
    if thresh.time == True:
        for i in range(start,end):
            if data[i].Greater(thresh):
                count += 1
            else:
                count = 0
            if count == winL:
                return i-winL+1
    else:
        for i in range(start,end):
            if data[i].Less(thresh):
                count += 1
            else:
                count = 0
            if count == winL:
                return i-winL+1
    return None


#data is one of the seven arrays created in the createDataArrayAll function

#start and end are real number values corresponding to the beginning and ending indexes

#threshLo is a swingData object with a boolean value for time that is true if searching withinRange threshold and false if searching OutofRange.

#threshHi is a swingData object with a boolean value for time that is true if searching withinRange threshold and false if searching OutofRange.

#winL is an real number value corresponding to the number of samples in a row we check against the thresh predicate

###IMPORTANT : : : threshHi and threshLo must have matching boolean values : : : IMPORTANT#######


def backSearchContinuityWithinRange(data, start, end, threshLo, threshHi, winL):
    count = 0
    if (threshLo.time == True and threshHi.time == True):
        for i in range(start,end):
            if (data[i].Greater(threshLo) and data[i].Less(threshHi)):
                count += 1
            else:
                count = 0
            if count == winL:
                return i-winL+1
    else:
        for i in range(start,end):
            if (data[i].Less(threshLo) or data[i].Greater(threshHi)):
                count += 1
            else:
                count = 0
            if count == winL:
                return i-winL+1
    return None



#data1 is one of seven arrays created with createDataArrayAll
#data2 is one of seven arrays created with createDataArrayAll

#start and end are real number values corresponding to the beginning and ending indexes

#thresh1 is a swingData object with a boolean value for time that is true if searching above threshold and false if searching below.

#thresh2 is a swingData object with a boolean value for time that is true if searching above threshold and false if searching below.

#winL is an real number value corresponding to the number of samples in a row we check against the thresh predicate

def searchContinuityAboveValueTwoSignals(data1, data2, start, end, thresh1, thresh2, winL):
    count = 0
    if (thresh1.time == True and thresh2.time == True):
        for i in range(start,end):
            if data1[i].Greater(thresh1) and data2[i].Greater(thresh2):
                count += 1
            else:
                count = 0
            if count == winL:
                return i-winL+1
    else:
        for i in range(start,end):
            if data1[i].Less(thresh1) and data2[i].Less(thresh2):
                count += 1
            else:
                count = 0
            if count == winL:
                return i-winL+1

    return None


#data is an array created with createDataArrayAll

#start and end are real number values corresponding to the beginning and ending indexes

#threshLo is a swingData object with a boolean value for time that is true if searching withinRange threshold and false if searching OutofRange.

#threshHi is a swingData object with a boolean value for time that is true if searching withinRange threshold and false if searching OutofRange.

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
            return [(i,i+winLength-1)] + searchMultiContinuityWithinRange(data, start + winLength, end, threshLo,threshHi,winLength)



