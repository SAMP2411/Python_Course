# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.readlines()
    with open("./Input/Names/invited_names.txt") as names:
        names_list = names.readlines()
        for name in names_list:
            name = name.strip("\n")
            with open(
                f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w"
            ) as invites:
                invites.write(letter_content[0].replace("[name]", name))
                for i in range(1, len(letter_content)):
                    invites.write(letter_content[i])
