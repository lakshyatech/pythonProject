# 1. Text File Handling:

# Reading from a text file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)

# Writing to a text file
with open("output.txt", "w") as file:
    data_to_write = "This is a sample text.\nPython File Handling is fun!"
    file.write(data_to_write)
    print("Data written to 'output.txt'")

# 2. CSV File Handling:

import csv

# Reading from a CSV file
with open("data.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)

import csv

# Writing to a CSV file
data_to_write = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "San Francisco"]
]

with open("output.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data_to_write)
    print("Data written to 'output.csv'")

# 3. JSON File Handling:

import json

# Reading from a JSON file
with open("data.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print("JSON Data:")
    print(data)

import json

# Writing to a JSON file
data_to_write = {"name": "John", "age": 28, "city": "Chicago"}

with open("output.json", "w") as jsonfile:
    json.dump(data_to_write, jsonfile)
    print("Data written to 'output.json'")