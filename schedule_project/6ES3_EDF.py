#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#EDF The timeline will represent 1 as excuting. The x-axis represent time and y-axis represent task order(J1,J2......).For example, J1 is excuting at time 0, there is 1 at (0,1)
class Task:
    def __init__(self, start, duration, deadline):
        self.start = start
        self.duration = duration
        self.deadline = deadline


def display(table):
    for i in table:
        for j in i:
            print(j, end=" ")
        print()


def taskSchedule():
    taskList = []
    numberOfTask = int(input('How many task: '))
    for i in range(numberOfTask):
        start = int(input(f"start time for task{i+1}: "))
        duration = int(input(f"duration for task{i+1}: "))
        deadline = int(input(f"deadline for task{i+1}: "))
        taskList.append(Task(start, duration, deadline))

        print()

    # find the max deadline
    maxDeadline = max([task.deadline for task in taskList])

    table = []
    for i in range(numberOfTask):
        sub = []
        for j in range(maxDeadline):
            sub.append(0)
        table.append(sub)

    startTimeList = [task.start for task in taskList]
    durationList = [task.duration for task in taskList]
    deadlineList = [task.deadline for task in taskList]

    for slot in range(maxDeadline):
        qualifiedIndex = []
        for index in range(len(startTimeList)):
            if startTimeList[index] != -1 and startTimeList[index] <= slot <= deadlineList[index]:
                qualifiedIndex.append(index)


        trueIndex = 0
        if len(qualifiedIndex) !=0:
            for index in range(len(qualifiedIndex)):
                if deadlineList[qualifiedIndex[index]] < deadlineList[qualifiedIndex[trueIndex]]:
                    trueIndex = index

            qualified = qualifiedIndex[trueIndex]
            table[qualified][slot] = 1

            durationList[qualified] -= 1
            if durationList[qualified] == 0:
                startTimeList[qualified] = -1
                deadlineList[qualified] = -1

    for duration in durationList:
        if duration > 0:
            print("IT IS NOT FEASIBLE!!!")
            return

    print("IT IS FEASIBLE!!!")
    display(table)

if __name__ == '__main__':
    taskSchedule()

