### give all the index values of vowels

vow=('a,e,i,o,u')
a=input('enter the string :')
for i in a:
	if i in vow:
		print(a.index(i))