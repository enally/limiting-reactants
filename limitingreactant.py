import re

molecular_dictionary = {
    'c':12,
    'h':1,
    'H':1,
    'C':12,
    'Na':200
    }
#new = 'ch3ch2(ch2)4ch2(ch)3(ch2)4(Na)4Na2'
new = raw_input('input first chemical formula: ')
new_maliable = new
answer = 0

# Seperate all bracketed groups from formula
myRegEx = re.compile(r"(\()(\w*)(\))(\d*)",re.I)
myMatches = myRegEx.findall(new)


print myMatches

# Add bracketed groups into formula again, removing original entries
for i in myMatches:
    for j in range(int(i[3])):
        new_maliable = new_maliable + i[1]
    new_maliable = new_maliable.replace(i[0] + i[1] + i[2] + i[3], '')
listed_new = list(new_maliable)

# Match letters to corresponding dictionary values
# loop through each letter and add value to answer variable
str_of_list = ''.join(listed_new)
new_reg = "[A-Z][a-z]?\d*"
the_test = re.findall(new_reg, str_of_list)
print the_test
for i,j in enumerate(listed_new):
    if j.isdigit() == True:
        for m in range(int(j)):
            answer += molecular_dictionary[listed_new[i-1]]
            
    else:
        if j in molecular_dictionary:
            answer += molecular_dictionary[j]

    
        
print answer
print new
print new_maliable

        





    
