given_str = input("Enter a string: ")
set_alphabets = {}

for i in given_str:
    if i in set_alphabets:
        set_alphabets[i] += 1
    else:
        set_alphabets[i] = 1

print("frequency :\n "+ str(set_alphabets))
