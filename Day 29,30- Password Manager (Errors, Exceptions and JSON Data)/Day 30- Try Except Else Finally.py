# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was Closed.")
#     raise KeyError("This is an error that I made up.")

height = float(input("Height:"))
weight = float(input("Weight: "))
if height > 3:
    raise ValueError("Human height should not be over than 3 meters.")
