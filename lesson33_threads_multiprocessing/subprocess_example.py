import subprocess
import datetime


print(datetime.datetime.now())
result = subprocess.run(['python', 'threads_example.py'], shell=True, capture_output=True, text=True)
print(result.stdout)
print(datetime.datetime.now())
print('We are gonna try call function')
subprocess.call(['python', 'threads_example.py'], shell=True, text=True)
print(datetime.datetime.now())
