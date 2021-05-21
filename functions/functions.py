from collections import OrderedDict
import sys

from setup.logConfig import log


def time_diff(time1, time2):
    """
    Calculates time difference.

    :param time1: time string on format hh:mm
    :param time2: time string on format hh:mm
    :returns: the difference in minutes as an integer.
    """
    time1 = time1.split(':')
    time2 = time2.split(':')
    time1 = int(time1[0])*60 + int(time1[1])
    time2 = int(time2[0])*60 + int(time2[1])
    return time2 - time1 if time2 >= time1 else -1


def percentage(tasks, task):
    """
    Calculates percentage

    :param tasks: a dictionnary with the format {task_name: total_time_of_task}
    :param task: name of task as a string
    :returns: percentage of a task compare to others in the dictionnary
    """
    total = 0
    for task_minutes in tasks.values():
        total += task_minutes
    return tasks[task]*100//total if total > 0 else 0


def read_file(filename):
    """
    Reads and parse a file.

    :param filename: path to a log file as a string
    :returns: order dictionnary with the content of the
    log file parsed.
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
    Writes dictionnary on a file.

    :param tasks:  a dictionnary with the format {task_name: total_time_of_task}
    :returns: none
    :writes content of dictionnary on a txt file
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
