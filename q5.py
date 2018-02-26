from Testing import testPenData, testCarData, average, stDeviation
from time import time

''' Random restart on testPenData() '''
def randResTestPenData(randRestarts=1):
    testAccuracy = []
    for testNum in range(0, randRestarts):
        nnet, ta = testPenData()
        testAccuracy.append(ta)
    return testAccuracy

def randResTestCarData(randRestarts=1):
    testAccuracy = []
    for testNum in range(0, randRestarts):
        nnet, ta = testCarData()
        testAccuracy.append(ta)
    return testAccuracy

if __name__ == '__main__':
    ''' Test Pen Data '''
    start = time()
    testAccuracy = randResTestPenData(5)
    # Calculate statistics
    maxTA = max(testAccuracy)
    meanTA = average(testAccuracy)
    stdevTA = stDeviation(testAccuracy)
    # Output to terminal
    print 'max:', maxTA
    print 'mean:', meanTA
    print 'stdev:', stdevTA
    # Output to file
    fout = open('NN Random Restarts on Test Pen Data.txt', 'w')
    fout.write('test accuracies: ' + str(testAccuracy) + '\n')
    fout.write('max: ' + str(maxTA) + '\n')
    fout.write('mean: ' + str(meanTA) + '\n')
    fout.write('stdev: ' + str(stdevTA) + '\n')
    end = time()
    executionTime = end - start
    fout.write('execution time: ' + str(executionTime) + ' seconds')
    print('execution time:', executionTime, 'seconds')
    fout.close()

    ''' Test Car Data '''
    start = time()
    testAccuracy = randResTestCarData(5)
    # Calculate statistics
    maxTA = max(testAccuracy)
    meanTA = average(testAccuracy)
    stdevTA = stDeviation(testAccuracy)
    # Output to terminal
    print 'max:', maxTA
    print 'mean:', meanTA
    print 'stdev:', stdevTA
    # Output to file
    fout = open('NN Random Restarts on Test Car Data.txt', 'w')
    fout.write('test accuracies: ' + str(testAccuracy) + '\n')
    fout.write('max: ' + str(maxTA) + '\n')
    fout.write('mean: ' + str(meanTA) + '\n')
    fout.write('stdev: ' + str(stdevTA) + '\n')
    end = time()
    executionTime = end - start
    fout.write('execution time: ' + str(executionTime) + ' seconds')
    print('execution time:', executionTime, 'seconds')
    fout.close()
