from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)

# User.__table__


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


# ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# session.add(ed_user)


session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])
session.commit()


our_user = session.query(User).filter_by(name='mary').first()
print(our_user.fullname)



# ed_user.name
# ed_user.nickname

