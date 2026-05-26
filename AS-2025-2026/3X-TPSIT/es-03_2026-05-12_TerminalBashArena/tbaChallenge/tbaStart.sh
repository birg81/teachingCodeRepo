#!/bin/bash

# Controllo se l'argomento classroom è stato fornito
if [ -z "$1" ]; then
	echo "Utilizzo: $0 <classroom>"
	exit 1
fi

CLASSROOM=$1
INPUT_FILE="$HOME/.tbaChallenge/classrooms/${CLASSROOM}.csv"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BASE_DIR="$HOME/${CLASSROOM}-${TIMESTAMP}"

# Verifica se il file CSV esiste
if [ ! -f "$INPUT_FILE" ]; then
	echo "Errore: Il file $INPUT_FILE non esiste."
	exit 1
fi

# Funzione per pulire le stringhe:
# 1. Converte in minuscolo
# 2. Rimuove accenti (usa iconv per traslitterare)
# 3. Rimuove spazi e apostrofi
clean_string() {
	echo "$1" | \
	iconv -f UTF-8 -t ASCII//TRANSLIT | \
	tr '[:upper:]' '[:lower:]' | \
	tr -d " '" | \
	sed "s/[^a-z0-9]//g"
}

# Crea la directory principale della sessione
mkdir -p "$BASE_DIR"

# Legge il file CSV riga per riga
# Si assume che il separatore sia la virgola
tail -n +2 "$INPUT_FILE" | while IFS=',' read -r lastname firstname || [ -n "$lastname" ]; do

	CLEAN_LAST=$(clean_string "$lastname")
	CLEAN_FIRST=$(clean_string "$firstname")

	# Salta le righe vuote (es. fine file)
	[ -z "$CLEAN_LAST" ] && continue

	# Definisce il percorso della sottocartella e del file .flag
	USER_DIR="${BASE_DIR}/${CLASSROOM}-${CLEAN_LAST}-${CLEAN_FIRST}"
	FLAG_FILE="${USER_DIR}/.flag"

	# Crea la cartella utente
	mkdir -p "$USER_DIR"

	# Crea il file .flag con il contenuto richiesto
	# Formato: classroom,lastname,firstname (originali o puliti? Qui usiamo i puliti per coerenza)
	echo ${CLASSROOM},${CLEAN_LAST},${CLEAN_FIRST}. > $FLAG_FILE

	# Imposta i permessi a -r--r--r-- (lettura per tutti, nessuna scrittura/esecuzione)
	chmod 444 $FLAG_FILE
done

echo "Operazione completata! vai in: $BASE_DIR"