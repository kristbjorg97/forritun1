
num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0 
list1 = [] # thus will be a list of all enterd numbers 
while (num_int >= 0 ):
    list1.append(num_int) #adds number to list1
    num_int = int(input("Input a number: "))
if(num_int < 0):
    max_int = max(list1)  
# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line
