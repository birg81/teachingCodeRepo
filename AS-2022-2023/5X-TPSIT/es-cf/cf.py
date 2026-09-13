def codeName(s = '', isFname = False):
# this function encodes both first and last names.
# for the first name, the second parameter must be set to True
# for the surname just do not indicate the second parameter or set it to False
	s = s.upper()
	code = ''.join([
		c
			for c in s
				if
					ord(c) in range(ord('B'), ord('Z') + 1) and
					c not in 'AEIOU'
	])
	return f"{code[0]}{code[2:4]}" if len(code) > 3 and isFname else f"{code}{''.join([c for c in s if c in 'AEIOU'])}XXX"[0:3]

def codeDate(bday = '2000-01-01', isMale = True):
# this function encode a date
# take a date in format 'YYYY-MM-DD' and returns the encoded date of birth
	return f"{bday[2:4]}{'ABCDEHLMPRST'[int(bday[5:7])-1]}{bday[8:] if isMale else 40 +int(bday[8:])}"

def codePlace(city = ''):
# this function loads codes from a file and searches for the code by city name
	for c in open('elencoComuniAttuali_20221011.csv').read().split('\n'):
		if c.split(',')[1] == city.upper():
			return c.split(',')[0]
	return 'Z999'

def placeDictionary():
# this function return a disctionary with zip code as key and city as value
	return {c.split(',')[0]:c.split(',')[1] for c in open('elencoComuniAttuali_20221011.csv').read().split('\n')}

def codeCheck(code):
# this function returns the check char (called CIN)
	check = [
		[
			1,	0,	5,	7,	9,	13,	15,	17,	19,	21,
			2,	4,	18,	20,	11,	3,	6,	8,	12,	14,
			16,	10,	22,	25,	24,	23
		],
		range(0, 26)
	]
	ck = 0
	for i in range(0, len(code)):
		ck += check[i % 2][ord(code[i]) - (65 if ord(code[i]) >= 65 else 48)]
	return chr(65 + ck % 26)

def code(lastname = '', firstname = '', bday = '', isMale = True, city = ''):
# this function combines the previous functions and leaves the final code
	p_code = f"{codeName(lastname)}{codeName(firstname, True)}{codeDate(bday, isMale)}{codePlace(city)}"
	return f"{p_code}{codeCheck(p_code)}"

if __name__ == '__main__':
	print(
		f'''{
			code(
				'Greco',
				'Biagio Rosario',
				'1981-08-17',
				True,
				'Castellammare di Stabia'
			)
		}'''
	)
