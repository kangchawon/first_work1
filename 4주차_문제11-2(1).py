def addNumber(num):
    if num < 1:
        return num
    else:
        return num + addNumber(num-1)

print(addNumber(100))

