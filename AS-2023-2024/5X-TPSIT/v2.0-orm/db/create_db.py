from db.database import Base, engine
from models.PersonModel import PersonModel
Base.metadata.create_all(engine)