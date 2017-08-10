
#coding=utf-8

import random

def guessNumGameForLimitNumberOfGuess(maxNumberOfGuess) :
    
    print '开始生成 0(含) ~ 100(不含) 之间的数字'

    max = maxNumberOfGuess
    
    randomNum = random.randint(0,100)

    randomNum = int(randomNum)
    #print '随机数 : ' + str(randomNum)

    userNum = -1
    
    
    while (userNum != randomNum) :

        userNum = raw_input('请猜该数字是多少 : ')
        
        userNum = int(userNum)

        #print '所猜数据 : ' + str(userNum) + ' ' + str(userNum > randomNum) + str(userNum - randomNum)

        if userNum > randomNum :
            print '大了 '
        if userNum < randomNum :
            print '小了'
        if userNum == randomNum :
            print '******************** 恭喜您猜正确了 ******************** \n\n\n\n\n\n\n ******* 重新开始 ********'
            printResult(maxNumberOfGuess)
        
        max -= 1
        if max == 0 :
            
            print '该数字是 : ' + str(randomNum) + ' 您猜错了 '
            print '*************************     GAME OVER     *************************\n\n\n\n\n\n*************************     重新开始     *************************'
            printResult(maxNumberOfGuess)
        print '您还剩余 ' + str(max) + ' 次可猜!'




def guessNumGameForSetRankings :
    
    degreeOfDifficulty = raw_input( '设定难度系数 : ' )
    
    degreeOfDifficulty = int(degreeOfDifficulty)
    
    print '开始生成 0(含) ~ ' + str(degreeOfDifficulty) + '(不含) 之间的数字'
    
    max = a
    
    randomNum = random.randint(0,100)
    
    randomNum = int(randomNum)
    #print '随机数 : ' + str(randomNum)
    
    userNum = -1
    
    
    while (userNum != randomNum) :
        
        userNum = raw_input('请猜该数字是多少 : ')
        
        userNum = int(userNum)
        
        #print '所猜数据 : ' + str(userNum) + ' ' + str(userNum > randomNum) + str(userNum - randomNum)
        
        if userNum > randomNum :
            print '大了 '
        if userNum < randomNum :
            print '小了'
        if userNum == randomNum :
            print '******************** 恭喜您猜正确了 ******************** \n\n\n\n\n\n\n ******* 重新开始 ********'
            printResult(a)
        
        max -= 1
        if max == 0 :
            
            print '该数字是 : ' + str(randomNum) + ' 您猜错了 '
            print '*************************     GAME OVER     *************************\n\n\n\n\n\n*************************     重新开始     *************************'
            printResult(a)
        print '您还剩余 ' + str(max) + ' 次可猜!'




printResult(5)



'''
    难度系数 （自己输入  在设定好的选项中选  ）
    猜测次数  (设定 不设定)
    排名  设置排名规则




设定难度系数 随机数最大值是多少 难度系数就是多少  记录猜对所用的次数 在同难度系数中进行排名

'''
