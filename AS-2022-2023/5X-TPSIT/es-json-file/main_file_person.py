'''
this file describe how-to python
1. can read a json file
2. convert in a python object
3. compute and filter python data
4. convert python object to json string
5. save json string in a json file
'''

# import json build-in module
import json

# open a json file
f = open('personList.json')

# convert textfile in dictionary
people = json.load(f)

# close file
f.close()

# print people
for p in people:
	print(p)

# filter under age people
under_age = [p for p in people if p['age'] < 18]

# convert object in a json_string
json_under_age_str = json.dumps(under_age)

# open output text file
f = open('under_age2.json', 'w')

# write string to file
f.write(json_under_age_str)

# close output file
f.close()
