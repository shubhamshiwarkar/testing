my_list = [5, 3, 8, 6, 2, 7]

minn = 0

for i in range(len(my_list) - 1):

    minn = i

    for j in range(i + 1, len(my_list)):

        if my_list[j] < my_list[minn]:
            minn = j

    temp = my_list[i]
    my_list[i] = my_list[minn]
    my_list[minn] = temp

print(my_list)
