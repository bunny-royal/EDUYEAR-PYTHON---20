## print all the numbers which are palindrome inside the list

nums=[541589,5161,65498,123321,221122,100001,1123]
for i in range(len(nums)):
	num=nums[i]
	temp=str(num)
	temp=temp[::-1]
	temp=int(temp)
	if temp==num:
		print('it is palindrome{}'.format(num))
	#else:
		#print('it is not palindrome{}'.format(num))