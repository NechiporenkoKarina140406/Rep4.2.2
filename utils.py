#Для обчислення факторіалу
def factorial (n):
    f = 1
    for i in range (2, n + 1):
        f * = i
    return f
#чи є число простим 
def check_prime():
n = int(input("Введи ціле число n="))
if n < 2:
    print("Число має бути 2 і більше")
    quit()
elif n == 2:
    print("Це  просте число")
