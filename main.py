# Pamela Petterchak
# CS 5170 Semester Project

# Things to do:
#    Add in fixed event things
#    Add in functionality for precedence constraints
#    Add in LST function
#    Read in from a file
#    Clean it up and make it pretty

# Define task classes
# class fixedTask:
#     def __init__(self, name, start, duration):
#         self.name = name
#         self.start = start
#         self.duration = duration

class todoTask:
    def __init__(self, name, duration, deadline, precedence):
        self.name = name
        self.duration = duration
        self.deadline = deadline
        self.precedence = precedence

# Define EDF and LST algorithms (inspired by source: https://github.com/vigneshkulo/realTimeSystems/tree/master/Scheduling%20Algorithms)
def EDF(todoTasks, startTime, endTime):
    currentTime = startTime         #set starting time
    totalTasks = len(todoTasks)     #set number of tasks
    completedTasks = []             #initialize completed tasks

    while(totalTasks > 0):
        # set initial next task
        nextTask = todoTasks[0]

        # loop through tasks
        for task in todoTasks:
            # check to see if deadline passed
            if task.deadline < currentTime:
                print("Error: task deadline passed:", task.name)
                return

            # check for earliest deadline
            if task.deadline < nextTask.deadline:
                nextTask = task

        # make sure there are no precedence constraints
        if len(nextTask.precedence) > 0:
            print("handle precedence later!")
            #code here
        # if no precedence constraints, schedule task
        else:
            # set end time
            endTime = currentTime + nextTask.duration
            # schedule
            print(currentTime, "to", endTime, ":", nextTask.name)
            # set new currentTime
            currentTime = endTime
            # add to completed tasks
            completedTasks.append(nextTask.name)
            # decremeent total tasks
            totalTasks = totalTasks - 1

        # if task is completed, remove it from list
        for task in todoTasks:
            for doneTask in completedTasks:
                if task.name == doneTask:
                    todoTasks.remove(task)

# Operational Code
startTime = 8   #start of day in military time
endTime = 16    #end of day in military time

#define todo tasks
task1 = todoTask("task 1", 0.5, 15, [])
task2 = todoTask("task 2", 2, 13, [])
task3 = todoTask("task 3", 4, 14, [])

#put tasks in an array
todoTasks = [task1, task2, task3]

#attempt EDF with todoTasks
EDF(todoTasks, startTime, endTime)
