# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#number = input('Введите число: ')
#sum = 0
#for i in number:
#    if i != '.':
#        sum += int(i)
#print('Сумма цифр равна:', sum)


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#N = int(input('Введите число: '))
#f = 1
#for i in range(N):
#    i += 1
#    f *= i
#    print(f, end = ' ')

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

#n = int(input('Введите число: '))
#some_list = [(1 + 1/n)**i for i in range(1, n+1)]
#print(f'Последовательность: {some_list}\nСумма равна: {sum(some_list)}')

# Реализуйте алгоритм перемешивания списка.

#def selection_sort(nums):
#    for i in range(len(nums)):
#        min_index = i
#        for j in range(i + 1, len(nums)):
#            if nums[j] < nums[min_index]:
#                min_index = j
#        nums[i], nums[min_index] = nums[min_index], nums[i]
        
#some_list = [1, 5, 4, 8, 9, 7]
#print(some_list)
#selection_sort(some_list)
#print(some_list)


