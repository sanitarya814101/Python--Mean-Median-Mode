import csv
from collections import Counter
with open('HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
# print(file_data)

new_data = []
for i in range(len(file_data)):
    num = file_data[i][2]
    new_data.append(float(num))

# print(new_data)

data = Counter(new_data)

modeDataForRange = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}

for Weight, occurence in data.items():
    if 50 < float(Weight) < 60:
        modeDataForRange['50-60'] += occurence
    elif 60 < float(Weight) < 70:
        modeDataForRange['60-70'] += occurence
    elif 70 < float(Weight) < 80:
        modeDataForRange['70-80'] += occurence

mode_range, mode_occurence = 0, 0

for range, occurence in modeDataForRange.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [
            int(range.split('-')[0]), int(range.split('-')[1])], occurence

mode = float((mode_range[0] + mode_range[1]) / 2)
print("Mode value of the data is: " + str(mode))
