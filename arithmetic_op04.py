#Create a variable called 'number' and assign it the three-digit number.
number=int(input("3 xonali sonni kiriting"))
#Find the 'number' first digit and assign to x1.
x1=number//100
#Find the 'number' second digit and assign to x2.
x2=(number%100)//10
#Find the 'number' third digit and assign to x3.
x3=(number%100)%10
#Create a variable called 'answer' and assign it the sum of the three digits.
answer=x2+x3+x1
#print the sum of the three digits.
print(answer)