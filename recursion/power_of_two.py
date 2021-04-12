#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
#Операцией возведения в степень пользоваться нельзя!

def is_power_of_two(N, power=1):
	if power == N:
		return "YES"
	if power > N:
		return "NO"
	power = power*2	 
	return is_power_of_two(N,power)

number=int(input("Enter number \n"))	
print(is_power_of_two(number))

  
