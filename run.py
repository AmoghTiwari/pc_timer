from datetime import datetime as dt
from time import sleep
from os import system
import notify2

def gettime():
    time=int(input("Enter time in minutes: "))
    #TODO
    #Add error handling for time
    return time
    

time_minutes=gettime()
time_seconds=time_minutes*60
start_time=dt.now()
print("Timer started at:",start_time.strftime("%H:%M:%S"), end=' ')
print("for %d minute." %(time_minutes))
sleep(2)
seconds_elapsed=0
while(seconds_elapsed<time_seconds):
    current_time=dt.now()
    seconds_elapsed=int((current_time-start_time).total_seconds())
    time_elapsed=str(int(seconds_elapsed/60))+" minutes and "+str(seconds_elapsed%60)+" seconds"
    seconds_remaining=time_seconds-seconds_elapsed
    time_remaining=str(int(seconds_remaining/60))+" minutes and "+str(seconds_remaining%60)+" seconds"
    print("Started At:",start_time.strftime("%H:%M:%S"))
    print("Time Remaining:",time_remaining)
    print("Time Elapsed  :",time_elapsed)
    sleep(1)
    system('clear')

print("Time Up")
notify2.init('Timer Up')
n=notify2.Notification("Time for a break!")
n.set_urgency(notify2.URGENCY_NORMAL)
n.show()
n.set_timeout(15000)
system('spd-say "your program has finished"')