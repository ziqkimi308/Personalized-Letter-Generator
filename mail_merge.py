"""
********************************************************************************
* Project Name:  Personalized Letter Generator
* Description:   It generates personalized letters for each name in list
* Author:        ziqkimi308
* Created:       2024-12-05
* Updated:       2024-12-05
* Version:       1.0
********************************************************************************
"""

# Open name list
with open("./name list.txt") as namelist:
    list = namelist.readlines()

# Open letter template
with open("letter template.txt") as letter_template:
    letter = letter_template.read()

# Replace the [name] with name in list
for name in list:
    stripped = name.strip()  # Remove whitespaces
    new_letter = letter.replace("[name]", stripped)

    # Create new letter
    with open(f"./Output/letter_for_{stripped}.txt", mode='w') as new:
        new.write(new_letter)

# 1. open name list
# 2. open template letter
# 3. strip every name in list
# 4. replace [name] with every stripped names
# 5. create new letter for every stripped names