# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

t_split = "a a a b c a a d c d d".split()
t_split2 = t_split
print(t_split)

for i in range(len(t_split)):
    count = 0
    for j in range(len(t_split2)):
        if t_split[i] == t_split2[j]:
           if count > 0: 
                t_split2[j] = t_split[i] + '_' + str(count)
                count += 1
           else:
                count +=1

print(t_split2)