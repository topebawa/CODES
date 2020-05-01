sum=0
numbers=[]
number=[]
for nums in range (100):
    if (nums%2==0):
        sum+=nums
        numbers.append(nums)
    if(nums%2!=0):
        sum+=nums
        number.append(nums)
print(numbers)
print(number)
