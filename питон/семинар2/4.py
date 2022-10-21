#Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

n = int(input("Введите число N: "))
array = []
for i in range (-n, n + 1):
    array.append(i)

position_1 = int(input("Введите позицию 1: "))
position_2 = int(input("Введите позицию 2: "))
answer = array[position_1 - 1] * array[position_2 - 1]
print(f"Ответ: {answer}")
