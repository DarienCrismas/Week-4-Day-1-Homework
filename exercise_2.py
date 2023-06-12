"""
Use python to read the file regex_test.txt and print the last name on each line using regular expressions and groups (return None for names with no first and last name, or names that aren't properly capitalized)
Hint: use with open() and readlines()

"""
"""
Expected Output:
Abraham Lincoln
Andrew P Garfield
Connor Milliken
Jordan Alexander Williams
None
None
"""
import re


with open("regex_test.txt") as f:
        data = f.readlines()
        

def name_test():
    name_pattern = re.compile("([A-Z][a-z]+) ?([A-Z][a-z]*?)? ([A-Z][a-z]+)")
    for name in data:
        match = name_pattern.search(name)   
        if match:
            if match.group(2) != None:
                yield f"{match.group(1)} {match.group(2)} {match.group(3)}"
            else:
                yield f"{match.group(1)} {match.group(3)}"
        if not match:
            yield None

test = name_test()

for name in data:
     print(next(test))
    