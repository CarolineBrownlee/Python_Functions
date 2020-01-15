# Python_Function Example:

# def create_person(first_name, last_name, age, occupation):
#     return {
#         "first_name": first_name,
#         "last_name": last_name,
#         "age": age,
#         "occupation": occupation,
#     }

# melissa = create_person("Melissa", "Bell", 25, "Software Developer")

# 1. Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.

def run(name):
    print(f"{name} went for a run.")

def swing(name):
    print(f"{name} is swinging.")

def slide(name):
    print(f"{name} went down the slide.")

def hide_and_seek(name):
    print(f"{name} played hide and seek.")

run("Joseph")
swing("Joseph")
slide("Joseph")
hide_and_seek("Joseph")

# 2. The following lists of children should be iterated, and the names sent to the appropriate functions.

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

for kids in running_kids:
    run(kids)

for kids in swinging_kids:
    swing(kids)

for kids in sliding_kids:
    slide(kids)

for kids in hiding_kids:
    hide_and_seek(kids)