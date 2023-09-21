import random
def generateRandomNumbers(randRange):
    
    randomList = []
    
    for i in range(0, randRange):
        n = random.randint(0,1)
        randomList.append(n)
        
    numbersList = [str(i) for i in randomList]
    allNos = "".join(numbersList)
    
    return allNos

def convertToBase10(num):
    newNum = str(num)
    ans = 0
    raiseToPow = 3
    for i in range(len(newNum)):
        ans += (int(newNum[i]) * pow(2, raiseToPow))
        raiseToPow -= 1
    return ans

randomNum = generateRandomNumbers(4)

print("4 digit random number: " + randomNum)
print("Base 10 value: " + str(convertToBase10(randomNum)))