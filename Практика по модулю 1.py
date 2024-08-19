grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list = list(students)
my_list.sort()

sum0 = sum(grades[0])
sum1 = sum(grades[1])
sum2 = sum(grades[2])
sum3 = sum(grades[3])
sum4 = sum(grades[4])

len0 = len(grades[0])
len1 = len(grades[1])
len2 = len(grades[2])
len3 = len(grades[3])
len4 = len(grades[4])

score0 = sum0 / len0
score1 = sum1 / len1
score2 = sum2 / len2
score3 = sum3 / len3
score4 = sum4 / len4

average_score = {my_list[0]: score0, my_list[1]: score1, my_list[2]: score2, my_list[3]: score3, my_list[4]: score4}
print(average_score)
