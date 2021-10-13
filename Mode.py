import csv
from collections import Counter
with open('HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
# print(file_data)

new_data = []
for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))

# print(new_data)

data = Counter(new_data)

modeDataForRange = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}

for height, occurence in data.items():
    if 50 < float(height) < 60:
        modeDataForRange['50-60'] + occurence
    elif 60 < float(height) < 70:
        modeDataForRange['60-70'] + occurence
    elif 70 < float(height) < 80:
        modeDataForRange['70-80'] + occurence

mode_range, mode_occurence = 0, 0

for range, occurence in modeDataForRange.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [
            int(range.split('-')[0]), int(range.split('-')[1])], occurence

# Mam, please check the mode one...
