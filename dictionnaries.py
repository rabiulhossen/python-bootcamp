
def invert_dictionary(original_dict):
    inverted_dict = {}

    # Iterate over each student and their courses in the original dictionary
    for student, courses in original_dict.items():
        # Iterate over each course for the student
        for course in courses:
            # If the course is not a key in the inverted dictionary, add it with an empty list as the value
            inverted_dict.setdefault(course, [])
            # Append the student to the list of students for the course
            inverted_dict[course].append(student)

    return inverted_dict

# Sample input dictionary
original_dict = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# Display the original dictionary
print("Original Dictionary:")
print(original_dict)

# Get and display the inverted dictionary
inverted_dict = invert_dictionary(original_dict)
print("\nInverted Dictionary:")
print(inverted_dict)


"""
    Original Dictionary:
{'Stud1': ['CS1101', 'CS2402', 'CS2001'], 'Stud2': ['CS2402', 'CS2001', 'CS1102']}

Inverted Dictionary:
{'CS1101': ['Stud1'], 'CS2402': ['Stud1', 'Stud2'], 'CS2001': ['Stud1', 'Stud2'], 'CS1102': ['Stud2']}

    
"""


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)

