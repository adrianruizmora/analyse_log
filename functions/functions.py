from collections import OrderedDict
import sys

from setup.logConfig import log


def time_diff(time1, time2):
    """
    Parameters: takes two strings with time format hh:mm
    returns: the difference in minutes as an integer.
    """
    time1 = time1.split(':')
    time2 = time2.split(':')
    time1 = int(time1[0])*60 + int(time1[1])
    time2 = int(time2[0])*60 + int(time2[1])
    return time2 - time1


def percentage(tasks, task):
    """
    Parameters: takes a dictionnary that contains {task_name: total_time_of_task}
    and a specific task as a string
    returns: the percentage of the total time of the task passed as argument,
    compare to all the others in the dictionnary.
    """
    total = 0
    for task_minutes in tasks.values():
        total += task_minutes
    return tasks[task]*100//total


def read_file(filename):
    """
    Parameter: path to a file
    returns: a ordered dictionnary with the content
    of the file parsed.
    """
    tasks = {}
    try:
        planning_file = open(filename)
    except FileNotFoundError:
        sys.exit("File not found, please try again.")

    log.info(f"filename : {filename}")
    with planning_file:
        for line in planning_file.readlines():
            line = line.partition(' ')
            key = line[2].strip()
            # checks if the line is not empty
            if key:
                time_values = line[0].split('-')
                time = time_diff(time_values[0], time_values[1])
                if key not in tasks:
                    # if the task does not exist adds it to the dictionnary
                    tasks[key] = time
                else:
                    # if the task is already on the dictionnary adds time to its value
                    tasks[key] += sum([time])
    log.info(f"disorder dictionnary :  {tasks}")
    log.info(
        f"Order dictionnary :  {OrderedDict(sorted(tasks.items(), key=lambda t: t[0]))}")
    # returns ordered dicionnary
    return OrderedDict(sorted(tasks.items(), key=lambda t: t[0]))


def write_file(tasks):
    """
    Parameters: takes a dictionnary
    Writes content with a specific format
    into a file .txt
    Return: none
    """
    output_file = open("output.txt", "w+")
    log.info(f"output file for filtered logs : output.txt")
    for task in tasks:
        # Number of espaces between words 
        empty_space_1 = ' '*(29-len(task)-len(str(tasks[task])))
        empty_space_2 = ' '*(5-len(str(percentage(tasks,task))))
        # length of line must be exactly of 43 caracters
        output_file.write(
            f"""{task}{empty_space_1}{tasks[task]} minutes{empty_space_2}{percentage(tasks,task)}%\n""")
    output_file.close()
