def fibonacci_pattern(n):
	if n<=1:
		return n
	else:
		return (fibonacci_pattern(n-1)+fibonacci_pattern(n-2))


n=int(input())
for i in range(0,2*n):
	for j in range(fibonacci_pattern(i)):
		print("*",end="")
	print()
 
# *
# *
# **
# ***
# *****
# ********
# *************
# *********************
# **********************************
