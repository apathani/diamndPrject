import csv
import unittest
import DiamondKinetics1





class SimpleTestCase(unittest.TestCase):
    def testA(self, data):
        data1 = data
        start = 0
        end = 28
        threshLo = DiamondKinetics1.SwingData(float(-99999),float(0),float(-99999),float(-99999),float(-99999),float(-99999),float(-99999))
        threshHi = DiamondKinetics1.SwingData(float(99999),float(0.55),float(99999),float(99999),float(99999),float(99999),float(99999))
        winLength = 8
        print(DiamondKinetics1.searchMultiContinuityWithinRange(data1, start, end, threshLo, threshHi, winLength))
        assert DiamondKinetics1.searchMultiContinuityWithinRange(data1, start, end, threshLo, threshHi, winLength) == [(20,27)]

    def testB(self, data):
        data1 = data
        data2 = data
        start = 0
        end = 28
        thresh1 = DiamondKinetics1.SwingData(-99999,0,-99999,-99999,-99999,-99999,-99999)
        thresh2 = DiamondKinetics1.SwingData(-99999,0,-99999,-99999,-99999,-99999,-99999)
        winLength = 8
        print(DiamondKinetics1.searchContinuityAboveValueTwoSignals(data1, data2, start, end, thresh1, thresh2, winLength))
        assert DiamondKinetics1.searchContinuityAboveValueTwoSignals(data1, data2, start, end, thresh1, thresh2, winLength) == 20

    def testC(self, data):
        data = data
        start = 0
        end = 28
        threshLo = DiamondKinetics1.SwingData(float(-99999),float(0),float(-99999),float(-99999),float(-99999),float(-99999),float(-99999))
        threshHi = DiamondKinetics1.SwingData(float(99999),float(0.55),float(99999),float(99999),float(99999),float(99999),float(99999))
        winLength = 8
        print(DiamondKinetics1.backSearchContinuityWithinRange(data, start, end, threshLo, threshHi, winLength))
        assert DiamondKinetics1.backSearchContinuityWithinRange(data, start, end, threshLo, threshHi, winLength) == 20

    def testD(self, data):
        data = data
        start = 0
        end = 28
        threshLo = DiamondKinetics1.SwingData(float(-99999),float(0),float(-99999),float(-99999),float(-99999),float(-99999),float(-99999))
        winLength = 3
        print(DiamondKinetics1.searchContinuityAboveValue(data, start, end, thresh, winLength))
        assert DiamondKinetics1.searchContinuityAboveValue(data, start, end, thresh, winLength) == 20


if __name__ == "__main__":
    data = DiamondKinetics1.createDataArrayAll("latestSwing.csv")
    for i in range(len(data)):
        print (data[i].axs)
    data1 = data
    start = 0
    end = 28
    threshLo = DiamondKinetics1.SwingData(float(-99999),float(0),float(-99999),float(-99999),float(-99999),float(-99999),float(-99999))
    threshHi = DiamondKinetics1.SwingData(float(99999),float(0.55),float(99999),float(99999),float(99999),float(99999),float(99999))
    winLength = 8
    print(DiamondKinetics1.backSearchContinuityWithinRange(data, start, end, threshLo, threshHi, winLength))
    assert threshLo.Less(threshHi)
    assert DiamondKinetics1.backSearchContinuityWithinRange(data, start, end, threshLo, threshHi, winLength) == 20
    print(DiamondKinetics1.searchMultiContinuityWithinRange(data1, start, end, threshLo, threshHi, winLength))
    assert DiamondKinetics1.searchMultiContinuityWithinRange(data1, start, end, threshLo, threshHi, winLength) == [(20,27)]

    threshLo = DiamondKinetics1.SwingData(float(-99999),float(0.55),float(-99999),float(-99999),float(-99999),float(-99999),float(-99999))
    threshHi = DiamondKinetics1.SwingData(float(99999),float(0),float(99999),float(99999),float(99999),float(99999),float(99999))
    print(DiamondKinetics1.searchMultiContinuityWithinRange(data1, start, end, threshLo, threshHi, 5))
    assert (DiamondKinetics1.backSearchContinuityWithinRange(data1, start, end, threshLo, threshHi, 5) == 0)
    assert DiamondKinetics1.searchMultiContinuityWithinRange(data1, start, end, threshLo, threshHi, 5) == [(0,4), (5,9), (10,14),(15,19)]
















