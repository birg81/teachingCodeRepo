'''
Codifico e decodifico un messaggio secondo il cifrario di Cesare e Vigenère
'''

# importo le funzioni per la cifratura e decodidica del messaggio
from enc_dec_lib import encode, decode, encodeV, decodeV
# importo la libreria per prelevare parametri da command line
import sys


'''
se sono presenti parametri da riga di comando li utilizzo!!!
>> il primo argomento del cmd line è il file stesso, quindi verrà filtrato!
- .join(): unisce gli elementi di un array in una stringa
'''

# se il numero di parametri è più che sufficiente ovvero > 2 -> msg + key
if len(sys.argv) > 2:
	# l'ultimo argomento lo userò invece come chiave
	msg = ' '.join(sys.argv[1: -1])
	key = sys.argv[-1]

# se è presente il messaggio ma non la chiave, pongo la chiave uguale a messagio
elif len(sys.argv) == 2:
	msg = sys.argv[1]
	key = sys.argv[1]

# se non ho inserito parametri chiedo il messaggio in input
else:
	msg = input('Insert your message: ').strip()
	# se il messaggio è vuoto o con spazi ne chiede uno valido
	while len(msg.strip()) == 0:
		msg = input('Insert a valid message: ').strip()
	# ripeto la procedura per la chiave
	key = input('Insert your key: ').upper().strip()
	while len(key.strip()) == 0:
		key = input('Insert a valid key: ').upper().strip()

'''
*** Cifrario di Cesare ***
- stampo dunque sia il messaggio originale
- sia il messaggio codificato
- sia la decodifica del messaggio codificato

*** Cifrario di Vigenère ***
- stampo il messaggio originario
- stampo la chiave
- stampo il messaggio codificato
- stampo il messaggio decodificato
'''
print(
f'''
Caesar Cipher
* msg:	{msg}
* enc:	{encode(msg)}
* dec:	{decode(encode(msg))}

Vigenère Cipher
* msg:	{msg}
* key:	{key}
* enc:	{encodeV(msg, key)}
* dec:	{decodeV(encodeV(msg, key), key)}
'''
)