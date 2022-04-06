#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Cyclic Executive

import functools


def my_gcd(list):
    min_number = min(list)
    length = len(list)

    gcd = 1
    for i in range(2, min_number + 1):
        count = 0
        for j in list:
            if j % i != 0:
                break
            else:
                count += 1
                if count == length:
                    gcd = i
    return gcd


def my_scm(list):
    max_number = max(list)
    length = len(list)
    multiple = functools.reduce(lambda a, b: a * b, list)
    scm = multiple
    for i in range(max_number, multiple + 1):
        count = 0
        for j in list:
            if i % j != 0:
                break
            else:
                count += 1
                if count == length:
                    scm = i
                    return scm

def display(ls, oneIteration):
    count = 0
    print("major cycle 1")

    for i in range(len(ls)):
        print(f'minor cycle{i+1}:', end=" ")
        for j in ls[i]:
            print(j, end=' ')
        print()
        count += 1
        if (count == oneIteration):
            print()
            print('major cycle 2')



def task():
    task_dict = dict()
    numberOfTask = int(input("How many tasks: "))
    print()
    for i in range(numberOfTask):
        period = int(input(f"The period for task{i + 1}: "))
        duration = int(input(f'duration for task{i + 1}: '))
        task_dict[i + 1] = [period, duration]
        print()
    ls = sorted(task_dict.items(), key=lambda x: x[1][0])
    task_dict = {}
    for item in ls:
        task_dict[item[0]] = item[1]

    period_list = [value[0] for value in task_dict.values()]
    minor_cycle = my_gcd(period_list)
    major_cycle = my_scm(period_list)
    print(f'minor cycle is {minor_cycle}')
    print(f'major cycle is {major_cycle}')

    # check if it is feasible
    smallest_period = list(task_dict.values())[0][0]


    duan = int(smallest_period / minor_cycle)


    oneP = [minor_cycle for i in range(duan)]
    length = len(oneP)

    schduele_dict = {}
    flag = True
    for key in task_dict.keys():
        if flag:
            count = 0
            for i in range(len(oneP)):
                initial_index = minor_cycle - oneP[i]
                if oneP[i] - task_dict[key][1] >= 0:
                    oneP[i] = oneP[i] - task_dict[key][1]
                    flag = True
                    end_index = minor_cycle - oneP[i] - 1
                    schduele_dict[key] = [i, initial_index, end_index]
                    break
                else:
                    count += 1
                    if count == length:
                        flag = False
                        break
                    else:
                        continue

    if flag:
        print('it is feasible!')

    else:
        print('It is not feasible')
        return

    big = [[0 for j in range(minor_cycle)] for i in range(int(major_cycle*2 / minor_cycle))]

    print()

    for key in schduele_dict.keys():
        p = task_dict[key][0]
        times = int(p/minor_cycle)
        start_row = schduele_dict[key][0]
        col_index1 = schduele_dict[key][1]
        col_index2 = schduele_dict[key][2]
        while start_row < 2*major_cycle/minor_cycle:
            for col in range(col_index1, col_index2+1):
                big[start_row][col] = key
            start_row += times


    display(big, major_cycle/minor_cycle)


if __name__ == '__main__':
    task()

