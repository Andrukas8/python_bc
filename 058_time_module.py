import time

print(time.ctime(0))  # shows when time started for the system

print(time.ctime(10000000))  # converting number of seconds into date and time

time_object = time.localtime()
# time_object = time.gmtime() # UTC time
# print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

# ------------------------------
# converting strings into time objects
time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)

# -----------------------------
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)  # converts tuple into time strings
# converts tuple into number of seconds since epoch
time_string_epoch = time.mktime(time_tuple)
print(time_string)
print(time_string_epoch)
