# Дано натуральное число N>1. Проверьте, является ли оно простым. 
# Программа должна вывести слово YES, если число простое и NO, если число составное. 

def is_prime(N, delitel=2):
	if delitel == N:
		return "YES"
	if N%delitel ==0 :
		return "NO"#,delitel
	else:
		delitel = delitel + 1
		return is_prime(N,delitel)

number=int(input("Enter number \n"))
print(is_prime(number))    
