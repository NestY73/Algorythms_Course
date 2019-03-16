#-------------------------------------------------------------------------------
# Name:        mean_number
# Purpose:     Homework_lesson1_Algorythms
#
# Author:      Nesterovich Yury
#
# Created:     16.03.2019
# Copyright:   (c) Nesterovich 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

num1 = int(input('Введите первое число:'))
num2 = int(input('Введите второе число:'))
num3 = int(input('Введите третье число:'))

if num1 < num2 < num3 or num3 < num2 < num1:
    print('Среднее:', num2)
elif num2 < num1 < num3 or num3 < num1 < num2:
    print('Среднее:', num1)
else:
    print('Среднее:', num3)
