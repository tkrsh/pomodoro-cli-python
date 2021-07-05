import time 
import os 
import sys
from tqdm import tqdm
 
 
time_cycle = int(sys.argv[1]) *60 
time_short_break = int(sys.argv[2]) *60
time_long_break = int(sys.argv[3]) *60 
cycles= int(sys.argv[4])
total_cycles = int(sys.argv[5]) 


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
            time.sleep(time_cycle)
            notify(0,(x+1))
            sys.stdout.write("\n \tShort Break of {} (Minutes) Duration has started\n".format(time_short_break))            
            time.sleep(time_short_break)
            notify(1,(x+1))
        
    

        sys.stdout.write("\nLong Break of {} (Minutes) Duration has started\n".format(time_long_break)) 
        notify(2,(i+1))
        time.sleep(time_long_break)
        sys.stdout.write("\nComplete Cycle ({}/{}) of Pomodoro is done\n\n".format(i+1,total_cycles))

        if i+1 == total_cycles:
            notify(3,(i+1))
            sys.stdout.write("\nComplete Pomodoro Cycle Has Ended !\n\n".format(i+1,total_cycles))


       
if __name__=='__main__':
    start_info()
    pomodoro()


 