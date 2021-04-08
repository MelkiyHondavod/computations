# Дано слово, состоящее только из строчных латинских букв. 
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.

def is_palindrome(word, c):
	Len = len(word)

	if c == Len//2:
		if word[Len-c-1] != word[c]:
			return "NO"
		else:
			return "Yes"	

	if word[Len-c-1] == word[c]:
		c = c + 1
		return is_palindrome(word,c)
	else:
		return "NO"	

slovo = input("Enter Word \n")
print(is_palindrome(slovo,0))
