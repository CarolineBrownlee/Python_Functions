# FUNCTIONS

# def list_fav_colors(name, *args, **kwargs)
# *args makes a list
# **kwargs is a dictionary of key, value pairs

def make_family(name, **brownlees):
    family_stuff = brownlees.items()
    family_str = f"We are the {name} family. "
    for title, person in family_stuff:
        family_str += f"The {title} is {person}. "
    return family_str

family = make_family("Brownlee", mom="Caroline", boy="Joseph")
other_family = make_family("Madison", grandmother="Nana Martha")

# print(family)
# print(other_family)

# FOR/IN LOOP
stuff = ["caroline", "41", "hendersonville", "555-555-5555"]
# print(stuff)
# good old FOR LOOP example
cap_stuff = []
for foo in stuff:
    cap_stuff.append(foo.capitalize())
# print(cap_stuff)

# MAP example (map takes a function as an argument and that function takes one of the things in the array as an argument)
cap_stuff = list(map(lambda foo: foo.capitalize(), stuff))
# print(cap_stuff)

# COMPREHENSION example (kind of how a ternary allows you to write a simple version of if/else...it's a shortened version of a for loop)
cap_stuff = [foo.capitalize() for foo in stuff]
# print(cap_stuff)

# COMPREHENSIONS can run on any collection. Here's a dictionary example:
profile = {
    "name": "Fred", 
    "age": 34,
    "address": "123 Sesame St."
}

#FOR/LOOP version
profile_strings = []
for key, value in profile.items():
    profile_strings.append(f"The key is {key}. The value is {value}")

# COMPREHENSION version
profile_strings = [f"The key is {key}. The value is {value}" for key, value in profile.items()]

print(profile_strings)


