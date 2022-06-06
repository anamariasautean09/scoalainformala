import time
import os
import json

start = time.time()

os.system(r"copy C:\Windows C:\Users\Anamaria\TestCopyFiles")

end = time.time()

total_time = end - start

filename = r'D:\ScoalaInformala\scoalainformala\bitdefender\results.json'
data = {'results':[]}

if os.path.isfile(filename) is False:
    raise Exception("File not found")

with open(filename) as file:
    data = json.load(file)

data['results'].append(total_time)

with open(filename, "w") as file:
    json.dump(data, file)
    print("New json file is created.")

print(data)
