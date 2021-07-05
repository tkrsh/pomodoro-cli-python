import time 
import os 
import sys
from tqdm import tqdm
 
 
time_cycle = int(sys.argv[1])   
time_short_break = int(sys.argv[2])  
time_long_break = int(sys.argv[3])  
cycles= int(sys.argv[4])
total_cycles = int(sys.argv[5]) 

def display_timer(duration):
    duration = duration *60
    for remaining in range(duration, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("\t{:2d} seconds remaining.".format(remaining)) 
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rComplete!            \n")


def notify(msg,x):
    
    if msg ==0:
        os.system("notify-send CycleStarted")
    if msg ==1:
        os.system("notify-send Short_Break_Started")

    if msg ==2:
        os.system("notify-send Long_Break_Started")
    if msg ==3:
        os.system("notify-send Pomodoro_Completed")
    

def start_info():

    message = "\nPomodoro Cycle Has Been Set Sucessfully! \n\n----------------------------------\nTime Per Pomodoro Cycle: {} Minutes \nSmall Break Duration : {} Minutes\nLong Break Duration : {} Minutes\nCycles before Long Break : {}\nTotal Cycles : {}\n----------------------------------\n\n".format(time_cycle,time_short_break,time_long_break,cycles,total_cycles)
    sys.stdout.write(message)  
    sys.stdout.flush()

def pomodoro():


    for i in tqdm(range(total_cycles)):

        for x in range(cycles):
            sys.stdout.write("\n\nPomodoro Cycle {} has started !\n".format(x+1))
            # time.sleep(time_cycle)
            display_timer(time_cycle)
            notify(0,(x+1))
            sys.stdout.write("\n \tShort Break of {} (Minutes) Duration has started\n".format(time_short_break))            
            # time.sleep(time_short_break)
            display_timer(time_short_break)
            notify(1,(x+1))
        
    

        sys.stdout.write("\nLong Break of {} (Minutes) Duration has started\n".format(time_long_break)) 
        notify(2,(i+1))
        # time.sleep(time_long_break)
        display_timer(time_long_break)
        sys.stdout.write("\nComplete Cycle ({}/{}) of Pomodoro is done\n\n".format(i+1,total_cycles))

        if i+1 == total_cycles:
            notify(3,(i+1))
            sys.stdout.write("\nComplete Pomodoro Cycle Has Ended !\n\n".format(i+1,total_cycles))


       
if __name__=='__main__':
    start_info()
    pomodoro()


 