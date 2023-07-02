# Read two text files containing integer values and print common values
import pandas

with open("file1.txt") as f1:
    lines1 = f1.readlines()
    with open("file2.txt") as f2:
        lines2 = f2.readlines()
        result = [int(l1.strip("\n")) for l1 in lines1 if l1 in lines2]

print(result)


list = [1, 2, 3]
# conditional List Comprehension
# new_list = [ item for item in list if item > 50 ]
new_list = [item * item for item in list]
print(f"new_list = {new_list}")

# Dictionary Comprehension
# 1. Using list
# new_dict = {new_key : new_value for item in list}
new_dict = {item: item * item for item in list}
print(f"new_dict using list = {new_dict}")
# 2. Using dictionary
# Conditional Dictionary comprehension
# new_dict = {new_key : new_value for (key,value) in dict.items( ) if test_condition}
dict = {"Sam": 95, "Dam": 79, "Ram": 43}
new_dict = {key: "pass" for (key, value) in dict.items() if value > 50}
print(f"new_dict using dict = {new_dict}")


# Iterate thorugh data in pandas
dictionary = {
    "name": ["Sam", "Ram", "Dam"],
    "score": [95, 79, 43],
}
data_frame = pandas.DataFrame(dictionary)
for index, row in data_frame.iterrows():
    print(row)  # [ prints each  rows data individually ]
    print(row.name)  # [ prints all data in the specific column ]
