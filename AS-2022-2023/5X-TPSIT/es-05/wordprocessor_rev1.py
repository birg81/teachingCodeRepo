'''
In this example we will create a very basic, command line wordprocessor
In this version are adding that fectures:
- file name request from cli or input
- print the old file lines
- add timing
- delete blank lines
'''

# for import file name from cli param
import sys

# for loggin time line
import time

# check file name
if len(sys.argv) > 1:
	fname = sys.argv[1]
else:
	# ask file name while it not void
	fname = ''
	while fname == '':
		fname = input("please, insert file name: ").strip().lower()

# open my file in append mode
f = open(
	fname,	# filename
	'a+'	# append mode and read
)

# move coursor on file begin
f.seek(0)

# print old line
print(f'{f.read().strip()}\n')

# current line I wrote
line = ''

# welcome message
print('hello, write whatever you want...')

# you will be able to write as long as you do not write the end
while line.lower() != 'end':
	# current time
	t = time.strftime("%d/%m/%Y %H:%M")

	# if not black line write it on file
	if line:
		f.write(f'{t} >> {line}\n')

	# get current line whitout space in edges of line
	line = input(f'{t} >> ').strip()

# close your file
f.close()

# exit by your program
print('<< END >>')
