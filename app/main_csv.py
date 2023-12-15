import csv

# Step 2: Open the CSV file
with open('employees.csv', 'r') as file:
    # Step 3: Create a CSV reader
    csv_reader = csv.reader(file)

    # Step 4: Read and process the data
    for row in csv_reader:
        print(row)

print("ended")