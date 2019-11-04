import csv
import unittest


class SwingData(object):
    def __init__(self):
        self.time = []
        self.axs = []
        self.ays = []
        self.azs = []
        self.wxs = []
        self.wys = []
        self.wzs = []




#extrapolate data from csv file, returns allData, a SwingData object comprised
#of seven data arrays corresponding to time, ax, ay, az, wx, wy, wz.
def createDataArrayAll(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file)
        allData = SwingData()
        for row in csv_reader:
            allData.time += [row[0]]
            allData.axs += [row[1]]
            allData.ays += [row[2]]
            allData.azs += [row[3]]
            allData.wxs += [row[4]]
            allData.wys += [row[5]]
            allData.wzs += [row[6]]
        return allData


#data is an array created with createDataArrayAll

#start and end are real number values corresponding to the beginning and ending indexes

#thresh is an real number corresponding to the threshold specified for data

#winL is an real number value corresponding to the number of samples in a row we check against the thresh predicate

def searchContinuityAboveValue(data, start, end, thresh, winL):
    for i in range(start,end):
        if data[i] > thresh:
            satisfies = True
            for j in  range(winL):
                if data[i+j] <= thresh or (i+j>end):
                    satisfies = False
                    break
            if satisfies:
                return i
    return None


#data is one of the sesven arrays created in the createDataArrayAll function

#start and end are real number values corresponding to the beginning and ending indexes

#threshLo is an real number value corresponding to the low end of the threshold

#threshHi is an real number value corresponding to the high end of the threshold

#winL is an real number value corresponding to the number of samples in a row we check against the thresh predicate

def backSearchContinuityWithinRange(data, start, end, threshLo, threshHi, winL):
    for i in range(start,end):
        if data[i] > threshLo and data[i] < threshHi:
            satisfies = True
            for j in  range(winL):
                if data[i+j] <= threshLo or data[i+j] >= threshHi or (i+j>end):
                    satisfies = False
                    break
            if satisfies:
                return i
    return None


#data1 is one of seven arrays created with createDataArrayAll
#data2 is one of seven arrays created with createDataArrayAll

#start and end are real number values corresponding to the beginning and ending indexes

#thresh1 is is an real number value corresponding to the threshold specified for data 1
#thresh2 is is an real number value corresponding to the threshold specified for data 2

#winL is an real number value corresponding to the number of samples in a row we check against the thresh predicate

def searchContinuityAboveValueTwoSignals(data1, data2, start, end, thresh1, thresh2, winL):
    for i in range(start,end):
        if data1[i] > thresh1 and data2[i] > thresh2:
            satisfies = True
            for j in  range(winL):
                if data1[i+j] <= thresh1 or data2[i+j] <= thresh2 or (i+j>end):
                    satisfies = False
                    break
            if satisfies:
                return i
    return None


#data is an array created with createDataArrayAll

#start and end are real number values corresponding to the beginning and ending indexes

#threshLo is an real number value corresponding to the low end of the threshold

#threshHi is an real number value corresponding to the high end of the threshold

#winL is an real number value corresponding to the number of samples in a row we check against the thresh predicates

def searchMultiContinuityWithinRange(data, start, end, threshLo, threshHi, winLength):
    currLength = 0
    inSeq = False
    startIndex = None
    ans = []
    for i in range(start,end):
        inSeq = False
        if data[i]>threshLo and data[i]<threshHi:
           if startIndex == None:
               startIndex = i
           currLength+=1
           inSeq = True
        if inSeq == False and currLength !=0:
            if currLength>=winLength:
                ans.append((startIndex,i-1))
            currLength = 0
            startIndex = None
    return ans


