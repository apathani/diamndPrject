import csv
import unittest
import DiamondKinetics1




class SimpleTestCase(unittest.TestCase):
    def testA(self):
        data1 = [0,324,4235,6,6,6,100,7,7,8,10,3,7,7,324,1234,23,4,234,24332,412]
        start = 2
        end = 12
        threshLo = 5
        threshHi = 10
        winLength = 3
        print(DiamondKinetics1.searchMultiContinuityWithinRange(data1, start, end, threshLo, threshHi, winLength))
        assert DiamondKinetics1.searchMultiContinuityWithinRange(data1, start, end, threshLo, threshHi, winLength) == [(3,5),(7,9)]

    def testB(self):
        data1 = [0,324,4235,6,6,6,100,7,7,8,10,3,7,7,324,1234,23,4,234,24332,412]
        data2 = [0,324,1,1,1,1,100,7,7,8,10,3,7,7,324,1234,23,4,234,24332,412]
        start = 2
        end = 12
        thresh1 = 5
        thresh2 = 6
        winLength = 3
        print(DiamondKinetics1.searchContinuityAboveValueTwoSignals(data1, data2, start, end, thresh1, thresh2, winLength))
        assert DiamondKinetics1.searchContinuityAboveValueTwoSignals(data1, data2, start, end, thresh1, thresh2, winLength) == 6

    def testC(self):
        data = [0,324,4235,6,6,101,100,7,7,8,10,3,7,7,324,1234,23,4,234,24332,412]
        start = 2
        end = 12
        threshLo = 5
        threshHi = 100
        winLength = 3
        print(DiamondKinetics1.backSearchContinuityWithinRange(data, start, end, threshLo, threshHi, winLength))
        assert DiamondKinetics1.backSearchContinuityWithinRange(data, start, end, threshLo, threshHi, winLength) == 7

    def testD(self):
        data = [0,324,4235,6,6,101,100,7,7,8,10,3,7,7,324,1234,23,4,234,24332,412]
        start = 2
        end = 12
        thresh= 5
        winLength = 3
        print(DiamondKinetics1.searchContinuityAboveValue(data, start, end, thresh, winLength))
        assert DiamondKinetics1.searchContinuityAboveValue(data, start, end, thresh, winLength) == 2


if __name__ == "__main__":
    data = DiamondKinetics1.createDataArrayAll("latestSwing.csv")
    for i in range(len(data)):
        print (data[i].axs)
    unittest.main()