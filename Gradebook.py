last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

#Created list of extra subjects
subjects = ["phyics", "calculus", "poetry", "history"]
#Created list of grades applicable to each new subject
grades = [98, 97, 85, 88]

#Manually create a 2D list with the two prior variables
gradebook = [["phyics", 98],
["calculus", 97],
["poetry", 85],
["history", 88]]

#Adding my new grades for computer science to my gradebook
gradebook.append(["computer science", 100])

#Adding grade for visual arts
gradebook.append(["visual arts", 93])

#Fixing grade for visual arts
gradebook[-1][-1] = 98

#Changing poetry to a pass/fail rather than numerical
gradebook[2].remove(85)
gradebook[2].append("Pass")
#gradebook[2][1] = "Pass"

#Creating a variable with both the current and past semesters grades
full_gradebook = last_semester_gradebook + gradebook

#Print commands
#print(gradebook)
print(full_gradebook)