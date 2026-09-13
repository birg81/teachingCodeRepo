# encoding col cifrario di Cesare
def encode(message):
	return caesar_cipher(message)

# decoding col Cifrario di cesare
def decode(message):
	return caesar_cipher(message, -3)

# encoding col cifrario di Vigenère
def encodeV(message, key):
	return vigenere_cipher(message, key)

# decoding col cifrario di Vigenère
def decodeV(message, key):
	return vigenere_cipher(message, key, True, True)

def caesar_cipher(msg = '', key = 3):
	'''
	Cifrario di Cesare, in base al valore della chiave questa funzione può
	essere usata sia per la codifica che per la decodifica
	'''
	# numero di simboli da codificare (26: lettere dell'alfabeto)
	M = ord('Z') - ord('A') + 1
	# per traslazioni di lunghezza maggiore di M le riporta nel range 0, M-1
	key = key % M
	# parola criptata
	msg_enc = msg.strip().upper()
	# se key % M = 0 ovvero se key = 0, 26, 52 ecc non fa nulla
	if key > 0:
		msg_enc = ''
		for l in msg.strip().upper():
			# controlla se l è compresa nel mio alfabeto
			if ord(l) >= ord('A') and ord(l) <= ord('Z'):
				# in tal caso codifica il carattere
				msg_enc += chr( ord('A') + ((ord(l) -ord('A') +key) %M) )
			else:
				# altrimenti lo prende invariato
				msg_enc += l
	return msg_enc

def vigenere_cipher(msg = '', key = '', sensing = True, decrypt = False):
	'''
	Questa funzione effettua coding e decoding di un messaggio col cifrario
	di Vigenère
	- msg: plain text message (messaggio in chiaro da codificare o decodificare)
	- key: la chiave
	- sensing: boolean
		- True: case sensitive (messaggio con maiuscole/minuscole)
		- False: case insensitive (messaggio tutto maiuscolo)
	- decript: boolean
		- True: effettua decoding (da codificato a testo in chiaro)
		- False: effettua encoding (da testo in chiaro a codificato)
	'''
	# da bool si trasforma in un intero 1 o -1
	decrypt = 1 if not decrypt else -1
	# la chiave è case insensitive
	key = key.strip().upper()
	# messaggio da decodificare
	msg_enc = msg.strip()
	# numero di simboli dell'alfabeto ovvero 26
	M = ord('Z') - ord('A') + 1
	# se la chiave è nulla non codifica e restituisce il messaggio in chiaro
	if len(key) > 0:
		i = 0	# indice per scorrere le lettere della chiave
		msg_enc = ''
		# scorriamo il messaggio in chiaro
		for l in msg.strip():
			'''
			sense è una variabile per determina se la variabile è maiuscola
			sense = 0 --> lettera maiuscola
			sense = 32 -> lettera minuscola
			'''
			sense = ord(l) & 32
			# encoding solo di carattere alfabetici!!
			if (ord(l) - sense) >= ord('A') and (ord(l) - sense) <= ord('Z'):
				'''
				ord() : resituisce il codice ASCII del carattere
				chr() : converte intero in carattere ASCII corrispondente
				L'algoritmo lavora con dei valori nell'intervallo 0,..,25.
				Quindi bisogna sottrarre il valore ASCII della lettera 'A' (65)
				sommare la corrispondente lettera della chiave e usare %,
				operatore resto per effettuare una traslazione circolare
				delle lettere e in fine risportare i valori nel range
				delle lettere sommando nuovamente 'A'
				'''
				msg_enc += chr(
					ord('A')
					+ (sense if sensing else 0)
					+ (
						ord(l)
						+ (ord(key[i]) + 1) * decrypt
						- 2 * ord('A')
						- sense
					) % M
				)
				i = (i + 1) % len(key)
			else:
				msg_enc += l
	return msg_enc if sensing else msg_enc.upper()