grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students) # list - преобразование  множества в список
students.sort() # sort - сортировка по алфавиту
a1 = sum(grades[0])/len(grades[0]) # sum - сумма чисел, len - сумма цифр
a2 = sum(grades[1])/len(grades[1])
a3 = sum(grades[2])/len(grades[2])
a4 = sum(grades[3])/len(grades[3])
a5 = sum(grades[4])/len(grades[4])
average = (a1,a2,a3,a4,a5)
dict_ = dict(zip(students,average)) # zip - попарное соединение
print(dict_)