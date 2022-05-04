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

# Define EDF and LST algorithms
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
                if len(nextTask.precedence) > 0:
                    print("skip task")
                else:
                    nextTask = task

        # schedule tasks
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
                for prec in task.precedence:
                    if prec == doneTask:
                        task.precedence.remove(prec)


def LST(todoTasks, startTime, endTime):
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

            taskSlack = (task.deadline - currentTime) - task.duration
            nextTaskSlack = (nextTask.deadline - currentTime) - nextTask.duration

            # check for least slack time
            if taskSlack < nextTaskSlack:
                if len(nextTask.precedence) > 0:
                    print("skip task")
                else:
                    nextTask = task

        # schedule tasks
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
                for prec in task.precedence:
                    if prec == doneTask:
                        task.precedence.remove(prec)

# Operational Code
startTime = 8   #start of day in military time
endTime = 16    #end of day in military time

#define todo tasks
task1 = todoTask("CpE 5170 Homework", 2, 15, [])
task2 = todoTask("Drive to Rolla", 2, 13, ["Fill up gas tank"])
task3 = todoTask("Fill up gas tank", 0.5, 10, [])
task4 = todoTask("Make a todo list", 1, 11, [])
task5 = todoTask("Watch favorite Netflix show", 2, 16, ["CpE 5170 Homework"])

#put tasks in an array
todoTasks = [task1, task2, task3, task4, task5]

#attempt EDF with todoTasks
print("---Attempting schedule with EDF---")
EDF(todoTasks, startTime, endTime)

#reset the array
todoTasks = [task1, task2, task3, task4, task5]
print("---Attempting schedule with LST---")
LST(todoTasks, startTime, endTime)
