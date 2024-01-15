from sqlalchemy.orm import sessionmaker
from model import User, engine

Session = sessionmaker(bind = engine)

session = Session()

session.add(User(email='email@email.com', secret='password'))
session.commit()

print(session.query(User).all()[0].email)