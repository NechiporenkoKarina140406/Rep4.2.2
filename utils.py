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
def is_power_of_five(num):
# Визначаємо , чи є число степенем 5
def is_power_of_five(num):
    power = 0
    while 5 ** power <= num:
        if 5 ** power == num:
            return True
        power += 1
    return False

# Приклад використання
number = int(input("Введіть число: "))
if is_power_of_five(number):
    print(f"{number} є степенем 5")
else:
    print(f"{number} не є степенем 5")
