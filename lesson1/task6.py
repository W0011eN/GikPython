#Задание 6
#Если фирма отработала с прибылью, вычислите рентабельность выручки. 
#Это отношение прибыли к выручке. 
#Далее запросите численность сотрудников фирмы и определите прибыль фирмы в 
#расчёте на одного сотрудника.

print ("Введите значение выручки")
v= int (input())
print ("Введите значение издержки")
i= int (input())
if v>i:
    print("Прибль")
    print ("Введите количество сотрудников в компании")
    c= int (input())
    print (f"Прибль компании из расчета на одного сотрудника: {(v-i)/c}" )
else:
    print("Убыток")
