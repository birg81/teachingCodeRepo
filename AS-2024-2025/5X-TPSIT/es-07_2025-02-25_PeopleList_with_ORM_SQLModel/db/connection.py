from sqlmodel import create_engine, SQLModel
from sqlalchemy.orm import sessionmaker

# Configurazione del database
DBNAME = 'PeopleDB'
USERNAME = 'root'
PASSWORD = ''
DATABASE_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@localhost/{DBNAME}'

# Crea l'engine per il database
engine = create_engine(
	DATABASE_URL,
	echo = True
)

# Crea una sessione
SessionLocal = sessionmaker(
	autocommit = False,
	autoflush = False,
	bind = engine
)

# Funzione di dipendenza per ottenere la sessione
def getConnection():
	con = SessionLocal()
	try:
		yield con
	finally:
		con.close()

# Funzione per creare le tabelle
def createDB():
	SQLModel.metadata.create_all(
		bind = engine
	)