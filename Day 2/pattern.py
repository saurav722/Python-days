#pattern
n=5

x=1;y=0

while(x<=n):
	while(y<=x-1):
		print("* ",end="")
		y+=1
	# printing next line for each row
	print("\r")
	y=0;x+=1