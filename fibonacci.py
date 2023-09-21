def fibonacci(n):
    listOfNums = []
    
    i = 0
    while(len(listOfNums) < n):
        if i == 0:
            listOfNums.append(0)
            i+=1
            continue
        elif i == 1:
            listOfNums.append(1)
            i+=1
            continue
        listOfNums.append(listOfNums[i-1] + listOfNums[i-2])
        i+=1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return listOfNums

print("Sum of the first Fibonacci: ")
print(fibonacci(50))
