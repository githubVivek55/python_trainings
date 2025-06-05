import time

a = time.localtime()

print(a)

print("Current Time:", a.tm_hour, ":", a.tm_min, ":", a.tm_sec)

if(a.tm_hour < 12):
    print("Good Morning")
elif(a.tm_hour < 18):
    print("Good Afternoon")
else:
    print("Good Evening")
