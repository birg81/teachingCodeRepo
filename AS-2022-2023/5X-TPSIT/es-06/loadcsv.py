'''
In a single line the following instructions were executed:
* reading of the file in reading mode.
* storing the file in a string.
* string trimming.
* division of text lines into one
* elimination of the header line.
* looping and division of rows into columns.
* elimination of the first column.
* conversion of values ​​in columns to float data type
'''
execution_t = [
	float(col.split(',')[1])
	for col in
		open('csv_esempio.csv', 'r')
			.read()
			.strip()
			.split('\n')[1:]
]

'''
A C-like approach was used.
Through a multiline printing instead of the different %f markers, the maximum, the lowest and the average have been passed.
ex: "I'm %d years old." % (17) // output: I'm 17 years old.
%f is the marker indicating a float value;
%.nf version% .nf, with n one number, indicates the number of decimal places (after the point)
'''
print(f'''
vals:\t%d
max:\t%.9f
avg:\t%.9f
min:\t%.9f
''' % (
	len(execution_t),
	max(execution_t),
	sum(execution_t)/len(execution_t),
	min(execution_t)
))

# import matplotlib for draw a execution time graphics
import matplotlib.pyplot as plt

'''
grap	is a graphic
ax	are axis
'''
grap, ax = plt.subplots()
ax.plot(
	range(1, 101),
	execution_t
)

ax.set_xlabel('task number')
ax.set_ylabel('execution time [s]')
ax.set_title('Execution of many tasks')

plt.show()