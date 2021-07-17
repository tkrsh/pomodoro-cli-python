"pomodoro cli for interactive pomodoro sessions"
import time # for sleep
import os
import sys
from tqdm import tqdm


time_cycle = int(sys.argv[1])
time_short_break = int(sys.argv[2])
time_long_break = int(sys.argv[3])
cycles = int(sys.argv[4])
total_cycles = int(sys.argv[5])


def display_timer(duration):
    """ displays timer """
    duration = duration * 60
    for remaining in range(duration, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rComplete!            \n")


def notify(msg):
    """ Send notification to system using notify-send"""
    if msg == 0:
        os.system("notify-send CycleStarted")
    if msg == 1:
        os.system("notify-send Short_Break_Started")

    if msg == 2:
        os.system("notify-send Long_Break_Started")
    if msg == 3:
        os.system("notify-send Pomodoro_Completed")


def start_info():
    """Display Pomodoro Info"""
    message = ("\nPomodoro Cycle Has Been Set Sucessfully!"
               "\n\n----------------------------------\n"
               "Time Per Pomodoro Cycle: {} Minutes \nSmall Break Duration : {} "
               "Minutes\nLong Break Duration : {} Minutes\nCycles before Long Break : {}"
               "\nTotal Cycles : {}\n----------------------------------\n\n"
               .format(time_cycle, time_short_break, time_long_break, cycles, total_cycles))
    sys.stdout.write(message)
    sys.stdout.flush()


def pomodoro():
    """Pomodoro cycle logic"""
    for i in tqdm(range(total_cycles)):

        for time_range in range(cycles):
            sys.stdout.write(
                "\n\nPomodoro Cycle {} has started !\n".format(time_range+1))
            # time.sleep(time_cycle)
            display_timer(time_cycle)
            notify(0)
            sys.stdout.write(
                "\n \tShort Break of {} (Minutes) Duration has started\n".format(time_short_break))
            # time.sleep(time_short_break)
            display_timer(time_short_break)
            notify(1)

        sys.stdout.write(
            "\nLong Break of {} (Minutes) Duration has started\n".format(time_long_break))
        notify(2)
        # time.sleep(time_long_break)
        display_timer(time_long_break)
        sys.stdout.write(
            "\nComplete Cycle ({}/{}) of Pomodoro is done\n\n".format(i+1, total_cycles))

        if i+1 == total_cycles:
            notify(3)
            sys.stdout.write(
                "\nComplete Pomodoro Cycle Has Ended !\n\n".format(i+1, total_cycles))


if __name__ == '__main__':
    start_info()
    pomodoro()
