start = input()
end = input()

first_start = int(start[0])
second_start = int(start[1])
third_start = int(start[2])
fourth_start = int(start[3])

first_end = int(end[0])
second_end = int(end[1])
third_end = int(end[2])
fourth_end = int(end[3])


for num_1 in range(first_start, first_end + 1):

    for num_2 in range(second_start, second_end + 1):

        for num_3 in range(third_start, third_end + 1):

            for num_4 in range(fourth_start, fourth_end + 1):

                if num_1 % 2 != 0 and num_2 % 2 != 0 and num_3 % 2 != 0 and num_4 % 2 != 0:
                    print(f'{num_1}{num_2}{num_3}{num_4}', end=' ')