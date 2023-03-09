import datetime
dt = datetime.datetime.now().replace(microsecond=0) #drop microseconds from datetime.
print(dt)