n = int(input("Enter the length of the sequence: ")) # Do not change this line
count_number = 3
num1 = 1
num2 = 2
num3 = 3
sum1 = 0 
print(num1)
print(num2)
print(num3)
while count_number < n:
   sum1= num1 + num2 + num3 
   count_number +=1 
   num1 = num2
   num2 = num3 
   num3 = sum1
   print(sum1)
   


