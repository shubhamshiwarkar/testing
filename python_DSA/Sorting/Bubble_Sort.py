my_list = [3, 5, 8, 6, 7, 2]

# sort_list =

while my_list != sorted(my_list):

    for i in range(len(my_list) - 1):

        if my_list[i] > my_list[i + 1]:
            c = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = c

    print(my_list)

print('-->', my_list)
