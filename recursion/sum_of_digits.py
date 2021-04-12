# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи нельзя использовать цикл, а также строки, списки, массивы

numer = int(input("Enter number \n"))
def sum(N, count=0):
	if N==0:
		return count
	else:
		count = count + N%10
		N = N//10
		return sum(N,count)
print(sum(numer))		