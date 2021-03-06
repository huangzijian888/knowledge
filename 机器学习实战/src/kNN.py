#coding: utf-8
from os import listdir
from numpy import *
import operator
def createDataSet():#创建数据集和标签
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):#创建分类器
    '''
    inX:用于分类的输入向量
    dataSet:训练数据集
    labels:标签
    k:选择最近邻居的数目
    '''
    #20-23行代码实现距离计算 
    dataSetSize = dataSet.shape[0]#.shape[]查看数组或矩阵的纬度
    #tile 
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    #27-29行 选择距离最小的k个点
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.iteritems(),
     #32行 排序
     key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def test1():#第一个例子测试
        group,labels=createDataSet()
        print str(group)
        print str(labels)
        print classify0([0.1,0.1],group,labels,3)
    
def file2matrix(filename):
        fr = open(filename)
        arrayOLines = fr.readlines()
        numberOfLines = len(arrayOLines)#得到文件行数
        returnMat = zeros((numberOfLines,3))#创建返回的Numpy矩阵
        classLabelVector = []
        index = 0
        for line in arrayOLines:#解析文件数据到列表
            line  = line.strip()
            listFromLine = line.split('\t')
            returnMat[index,:] = listFromLine[0:3]
            classLabelVector.append(int(listFromLine[-1]))
            index+=1
        return returnMat,classLabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals-minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet-tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals

def datingClassTest():#针对约会网站的测试
    hoRatio = 0.15
    datingDataMat,datingLabels=file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m=normMat.shape[0]
    numTestVecs = int (m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],\
            datingLabels[numTestVecs:m],4)
        print "the classifier came back with: %d,the real answer is: %d"\
            % (classifierResult,datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount +=1.0
    print "the total error rate is: %f"%(errorCount/float(numTestVecs))

def img2vector(filename):
    returnVect = zeros((1,1024))
    fr= open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int (lineStr[j])
    return returnVect


def handwritingClassTest():
    hwLabels=[]
    trainingFileList=listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int (fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')
    errorCount =0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int (fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest,\
            trainingMat,hwLabels,3)
        print "the classifier came back with: %d,the real answer is:%d"\
            % (classifierResult,classNumStr)
        if(classifierResult != classNumStr): errorCount +=1.0
    print "\nthe total number of errors is:%d"% errorCount
    print "\nthe total error rate is:%f" %(errorCount/float (mTest)) 





