from uvicorn import run
from fastapi import FastAPI

app = FastAPI(
	title = ''
)
@app.get
if __name__ == '__main__':
	run(
		'main:app',
		http = 'httpttols',
		host = '0.0.0.0',
		port = 8080,
		reload = True
	)