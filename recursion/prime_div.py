# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  

def divide(N, k=2):
	if N==1:
		return 0
	if N%k == 0:
		print(k)
		N=N//k
		return divide(N)
	if N%k != 0:
		k=k+1
		return divide(N,k)

divide(115)