from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///pdf.db', echo=False) # 
connection = engine.connect() # 
Base = declarative_base()


class Pdf(Base):
    __tablename__ = 'pdfs'

    id = Column(Integer, primary_key=True)
    author = Column(String)
    creation_date = Column(String)
    modification_date = Column(String)
    creator = Column(String)
    status = Column(String)
    text = Column(String)

    def __repr__(self):
        return "<Pdf(author='%s', creation_date='%s', modification_date='%s', creator='%s', status='%s', text='%s')>" % (
            self.author, self.creation_date, self.modification_date, self.creator, self.status, self.text)

# User.__table__


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


# ed_user = User(author='ed', creation_date='Ed Jones', modification_date='edsnickname')
# session.add(ed_user)




def get_doc_text_in_dictionary():
    file_path = 'C:\_My_Files\_FA\_ETUDES\Python\py-code\sqlAlchemy_basic_example_in_python\carhovchadjijffq_text.txt'
    with open(file_path) as feed:
        text = feed.read()
        # doc_text_in_dictionary = {"text": text, }
        return text


msg_f = get_doc_text_in_dictionary()

"""
session.add_all([
    Pdf(author='wendy', creation_date='Wendy Williams',
        modification_date='windy', creator='me', status='ok', text='bla'),
    Pdf(author='mary', creation_date='Mary Contrary',
        modification_date='mary', creator='me', status='ok', text=msg_f),
    Pdf(author='fred', creation_date='Fred Flintstone',
        modification_date='freddy', creator='me', status='ok', text='bla')
])
session.commit()
"""

our_pdf = session.query(Pdf).filter_by(author='fred').first()
print(our_pdf.text)


# ed_user.author
# ed_user.modification_date
