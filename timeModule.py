import time

seconds = time.time()

print(seconds)

localtime = time.ctime(seconds)

time.sleep(2)

print(f"local time {localtime}")

result = time.localtime(seconds)
print(result)