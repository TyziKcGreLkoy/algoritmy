bubble_list = [4, 49, 23, 30, 43, 21, 1, 31, 15, 19]
for j in range(len(bubble_list) - 1):
    for i in range(len(bubble_list) - 1):
        print(j, i)
        if bubble_list[i] > bubble_list[i + 1]:
            p = bubble_list[i + 1]
            bubble_list[i + 1] = bubble_list[i]
            bubble_list[i] = p
print(bubble_list)
