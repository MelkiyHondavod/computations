
'''Код без коментариев (почти)'''
'''Код c  коментами ниже , строка 49 (лучше смотреть его - там понятнее)'''

start   = int(input(' Start : '))
finish  = int(input('Finish : '))
primes = [0] 
# забиваем массив 
if start != 1:
    for a in range(1,start):
        primes.append(0)

for a in range(start,finish + 1):  
    primes.append(a)
    a = a + 1 
# определяем значение i для функции
if start == 1 :
    i = 1
else:
    i = start - 1 

n = i + i 
# сам алгоритм 
def sieve(primes,n,i):
    i  = i + 1
    n = 0 
    if i <= finish: 
        if primes[i] != 0:
            n = i + i 
            while n <= finish :
                primes[n] = 0
                n = n + i 
            sieve(primes,n,i)
        else: 
            sieve(primes,n,i)  
    else:
        if 1 in primes:
            primes.remove(1)
        result = set(primes)
        result.remove(0)
        result_message = 'Your prime digits - ',result
        print('result is ',result) 
sieve(primes,n,i)
  



""" Код с коментариями """


'''получаем промежуток в ктором программма будет искать простые числа '''
start   = int(input(' Start : '))
finish  = int(input('Finish : '))

""" составляем массив с которым бедет потом работать функция"""
primes = [0] # сразу ставим 0 из -за здвига индексов (так просто намнoго удобнее работать)
#например primes = [1,2,3,4,5]
#если не сдвигать ,то primes[0]  это 1 , primes[1] это 2 и т.д
#а если сдвинуть , то primes[0]  = 0 , primes[1] = 1 цифре и т.д

if start != 1: # если start не равно 1 то мы будем забиваем нулями , потому что в
# функции будет намного труднее сделать сдвиг из-за начального значения.
# Eсли бы начальное значение было бы равно всегда 1 то не надо было бы забивать нулями 
    for a in range(1,start): # забиваем нулями все пространство до начального значения (start)
        primes.append(0)

'''теперь уже забиваем массив  цифрами до конечного значения (обычный цикл for )'''
for a in range(start,finish + 1): # "+1" из -за cдивга индексов  
    primes.append(a)
    #print(a)
    a = a + 1 
print(primes)

'''Обьявляю переменные нужные для работы программы '''
if start == 1 :
    i = 1
else:
    i = start - 1 # ствим I сразу на место первого элемента не равного нулю (начального значения)
    # "-1" потому что при  входе в функцию I сразу же увеличивается 
    # и чтоб мы не пропустили из -за этого число простое мы отнимем 1 
    
n = i + i # переменная для реализации поиска чисел больше I и их удаления это как 2i

def sieve(primes,n,i):
    i  = i + 1 # увеличиваем i (переходим в след.запуске функции к след.числу)
    n = 0      # обнуляем n  с прошлого прохода функции 
    print('ineration == ',i)
    if i <= finish: # пока I не больше допустимого значение которое ввел пользователь
        if primes[i] != 0: # и если это число не 0
            n = i + i # реалзуем через n принцып работы алгоритма 
            while n <= finish :
                print("I'm deleting ",n)
                primes[n] = 0 # забтваем n нулем потому что оно не простое
                n = n + i # увеличиваем n чтоб цикл дальше пошел искать число кратноe i
            print('-----------') # чтоб было удобнее просматривать историю (отделяет)
            sieve(primes,n,i) # после цикла запускаем функцию чтоб перейти к следующему числу 
        else: # ну а если оно все-таки 0 то заупскаем функцию и все 
            #( i увеличивается при каждом проходе функции так что  увеличивать не надо)
            print(' уже забито нулем')
            sieve(primes,n,i)  
    else:
        if 1 in primes: # 1 не протсое число поэтому удаляем его из массива (если оно там есть)
            primes.remove(1) 
        result = set(primes) # превращаем результат во множество чтоб не удалять  нули 
        result.remove(0) # поскольку это множество то там останется ноль полюбому поэтому мы его удалим
        result_message = 'Your primes : ' + str(result)
        print(result_message)
        # к сожалению множество нельзя отсортировать поэтому 
        # простые числа будут находится в "неправильном" порядке 
sieve(primes,n,i)


   
