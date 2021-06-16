a=[0,1,2,9,7,6,4,96,101]
even_count,odd_count=0,0
for i in a:
	if i%2==0:
		even_count +=1
	else:
		odd_count +=1
		print('Even numbers count is {}'.format(even_count))
		print('odd numbers count is {}'.format(odd_count))