## check whether list is palindrome or not

nums=[1,2,2,2,1,5]
temp=nums[::-1]
if temp==nums:
		print('it is palindrome{}'.format(nums))
else:
		print('it is not palindrome{}'.format(nums))