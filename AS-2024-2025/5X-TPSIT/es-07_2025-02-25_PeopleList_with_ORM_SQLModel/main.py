import uvicorn
from fastapi import FastAPI
from db.connection import createDB  # Importa la funzione di creazione del DB
from router.peopleRouter import router as people_router # Importa le rotte CRUD

# Inizializza FastAPI
app = FastAPI(
	title = 'People List Manager',
	decription = 'Routing and orm with SQLModel'
)

@app.get('/')
async def home():
	return {
		'msg': 'FastAPI: Just run'
	}

# Include le rotte nel progetto FastAPI
app.include_router(people_router)

if __name__ == '__main__':
	createDB()  # Assicurati che il DBMS venga creato all'avvio e avviato
	uvicorn.run(
		'main:app',
		http = 'httptools',
		host = '0.0.0.0',
		port = 8000,
		reload = True
	)