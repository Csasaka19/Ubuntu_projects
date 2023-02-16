# SQLAlchemy is a library that facilitates the communication between Python programs and databases

from sqlalchemy import Column, String, CHAR, VARCHAR, create_engine, ForeignKey, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = "Person"
    
    name = Column("name", CHAR(20))
    person_id = Column("ID", VARCHAR(15), primary_key=True)
    department = Column("Department", VARCHAR(25))
    Birth_year = Column("YOB", INTEGER)
    Bio = Column("Bio", String)
    
    def __init__(self, name, person_id, department, Birth_year, Bio):
        self.name = name
        self.person_id = person_id
        self.department = department
        self.Birth_year = Birth_year
        self.Bio = Bio
        
    def __repr__(self) -> str:
        return super().__repr__()
    
engine = create_engine("mysql:///test", echo=True)
Base.metadata.create_all(bind=engine)
    
Session = sessionmaker(bind=engine)
session = Session()

Incognito = Person("CC", "234-mm", "Human Resource", 2002, "Huwezi niona")

session.add(Incognito)

session.commit()