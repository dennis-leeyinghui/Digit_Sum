answer = input("Enter an integer")
length = len(answer)

print ("Length of Input is : ",  length)

sum = 0

for a in range(length):
    length -= 1
    print (answer[length])
    sum = sum + int(answer[length])
    
print ("Sum of digit is : ", sum)