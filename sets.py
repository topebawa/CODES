#sets
#curlybracket(strings),{'value','value','value','value',....}
#curlybracket(integer),{value,value,value,value,....}
#|--union
#&-- intersection
#- -- difference
#^ -- sysmmetric diiference

num1={1,2,3,4,5,6,7,9,20}
num2={10,11,12,18,9,15,20}
print(num1|num2)
#prints the two sets w/o repeating values
print(num1&num2)
#prints values common from the two sets
print(num1-num2)
#prints values in the num1 set that are not present in the num2
print(num2-num1)
#prints values in num2 set that are not present in the num1
print(num1^num2)
#prints the two sets w/o printing the values present in both 
