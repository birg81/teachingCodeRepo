from model.Models import SuperHero
from db.getConnection import getConnection
from fastapi import APIRouter, HTTPException

router = APIRouter(
	tags = ['Users'],
	prefix = '/api/v1.0/superhero'
)
# rHeroes dove r sta per READ del C[R]UD
def rHeroes(condition: str = ''):
	condition = f'WHERE {condition}' if condition else ''
	q = 'SELECT id, supername, firstname, lastname FROM SuperHeroes {} ORDER BY supername;'.format(condition)
	con = getConnection()
	if con:
		try:
			cur = con.cursor()
			cur.execute(q)
			rs = cur.fetchall()
			if len(rs) > 0:
				return [
					SuperHero(
						id = hero[0],
						supername = hero[1],
						firstname = hero[2],
						lastname = hero[3]
					)
					for hero in rs
				]
			else:
				return []
		finally:
			cur.close()
			con.close()
	else:
		return []
# cudHeroes dove CUD sta per READ/UPDATE/DELETE del [C]R[U][D]
# questa funzione fa 3 cose in una
# s: SuperHero|None = None significa che s può essere un oggetto o nulla e di default è nulla
def cudHeroes(kind: str = 'c', id: int = -1, s: SuperHero | None = None) -> int:
	q = {
		'c': 'INSERT INTO SuperHeroes (firstname, lastname, supername) VALUES ("{}", "{}", "{}");'.format(
			s.firstname, s.lastname, s.supername
		) if s else 'INSERT INTO SuperHeroes (firstname, lastname, supername) VALUES ("", "", "");',
		'u': 'UPDATE SuperHeroes SET firstname="{}", lastname="{}", supername="{}" WHERE id={};'.format(
			s.firstname, s.lastname, s.supername,
			id
		) if s else 'UPDATE SuperHeroes SET id=-1 WHERE id=-1;',
		'd': 'DELETE FROM SuperHeroes WHERE id={};'.format(id)
	}[kind.lower()]
	con = getConnection()
	if con:
		try:
			cur = con.cursor()
			cur.execute(q)
			con.commit()
			return cur.rowcount
		finally:
			cur.close()
			con.close()
	else:
		return -1

@router.get('/')
async def getSuperHeroes():
	return rHeroes()

@router.get('/{id}')
async def getSuperHeroById(id: int = 0):
	hero = rHeroes(f'id={id}')
	if len(hero) > 0:
		return hero[0]
	else:
		raise HTTPException(
			status_code = 404,
			detail = f'Not found superhero with id {id}!'
		)

@router.post('/')
async def createSuperHero(s: SuperHero | None = None):
	if s and cudHeroes(kind = 'c', s = s) > 0:
		return s
	else:
		raise HTTPException(
			status_code = 400,
			detail = 'Hai problemi ad inserire Eroe'
		)

@router.put('/{id}')
async def modifySuperHero(id: int = -1, s: SuperHero | None = None):
	if s and cudHeroes(kind = 'u', id = id, s = s) > 0:
		s.id = id
		return s
	else:
		raise HTTPException(
			status_code = 400,
			detail = f'Hai problemi a modificare eroe con id {id}'
		)

@router.delete('/{id}')
async def removeSuperHero(id:int = -1):
	if cudHeroes(kind = 'd', id = id) > 0:
		raise HTTPException(
			status_code = 200,
			detail = f'Hai rimosso correttamente SuperHero con id {id}'
		)
	else:
		raise HTTPException(
			status_code = 400,
			detail = f'Hai problemi ad eliminare eroe con id {id}'
		)