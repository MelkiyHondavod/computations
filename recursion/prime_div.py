# Дано натуральное число N>1. Выведите все простые множители этого числа k в порядке неубывания с учетом кратности.  

def divide(N, k):
  if n == 1:
    return k
  else:
    if n % k == 0:
      print(k)
      n = n // k
    if n % k != 0:
      k = k + 1
  divide(n,k)
 

divide(8, 2)