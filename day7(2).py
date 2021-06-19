### reverse the words of string

txt=('hello world happy birthday')
x=txt.split()
y=x[::-1]
txt=" ".join(y)
print(txt)