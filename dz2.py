# -*- coding: utf-8 -*-
"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
 а некоторые – гербом. Определите минимальное число монеток, 
 которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и
 той же стороной. Выведите минимальное количество монет,
 которые нужно перевернуть
"""
'''
n=int(input("Сколько монет лежит на столе? : "))
count_head=0;
count_tail=0;

for i in range(n):
    status=int(input("Орёл(1) или решка(0)? "))
    if status==1:
        count_head+=1
    else:
        count_tail+=1

if count_head >= count_tail:
    print("Минимальное число монет для переворота= ", count_tail)
else: 
    print("Минимальное число монет для переворота= ", count_head)
'''
    
    
"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y
(X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""

"""    
#Петя задумал два числа
X=int(input(" Введи Х, задуманный Петей ="))
Y=int(input(" Введи Y, задуманный Петей ="))
S=X+Y
P=X*Y
# Петя называет две подсказки
print("X+Y= ",S)
print("X*Y= ",P)
print()

# Катя, проведя расчёт, отвечает, учитывая a*x*x+b*x+c=0 и Y*Y-S*Y+P=0:
y=0
x=0
D=S*S-4*P
Y1=(S+D**0.5)/2
Y2=(S-D**0.5)/2
if Y1>0:
    y=Y1
else:
    y=Y2
x=S-y
print("Два числа равны", x," и", y)
"""

"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
 не превосходящие числа N.

"""

N = int(input("Введите число N: "))
k = 0
power_of_two = 1

while power_of_two <= N:
    print(power_of_two)
    k += 1
    power_of_two = 2 ** k

    

