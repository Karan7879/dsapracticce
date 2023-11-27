# Input : 1 2 3 4 5
# Output : 3

# Input : 1 2 3
# Output : 2

def meanofarray(arr,n,num,index):
    if index==n:
        return num
    print(arr,n,num,index)
    return meanofarray(arr,n,num+arr[index],index+1)

    


arr = [1,2,3,4,5]
n = len(arr)

print(meanofarray(arr,n,0,0))

def getbinary(number):
    # print(number)

	# Base case
	if number == 0:
		return 0
	
	# Recursion call and storing the result
	smallans = getbinary(number // 2)
    # print(number)
	
	return number % 2 + 10 * smallans

# Driver Code
decimal_number = 10
print(getbinary(decimal_number))




