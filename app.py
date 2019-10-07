my_name = 'arpit'
print("My name: "+my_name)
given_str = input("Enter a string: ")

set_alphabets_common = {'a': 0,'r': 0,'p': 0,'i': 0,'t': 0}

for key in given_str:
    if key == 'a':
        set_alphabets_common[key] = set_alphabets_common[key]+1
    if key == 'r':
        set_alphabets_common[key] = set_alphabets_common[key]+1
    if key == 'p':
        set_alphabets_common[key] = set_alphabets_common[key]+1
    if key == 'i':
        set_alphabets_common[key] = set_alphabets_common[key]+1
    if key == 't':
        set_alphabets_common[key] = set_alphabets_common[key]+1


print(set_alphabets_common)
