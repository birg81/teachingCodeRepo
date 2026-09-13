'''
In this example we will create a very basic, command line wordprocessor
'''

# open my file in append mode
f = open(
	'wordprocessor.txt',	# filename
	'a'	# append mode
)

# current line I wrote
line = ''
# welcome message
print('hello, write whatever you want...')

# you will be able to write as long as you do not write the end
while line.strip().lower() != 'end':
	# write on file current line
	f.write(f'{line.strip()}\n')
	# get current line
	line = input('>> ')

# close your file
f.close()

# exit by your program
print('<< END >>')