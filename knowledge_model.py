from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__='articles'
	articles_id=Column(Integer, primary_key = True)
	name = Column(String )
   	topic= Column(String)
   	rate = Column(Integer)


   	def __repr__(self):
		return ("Article Name: {}\n"
               	"Topic: {} \n"
                "Rate: {}").format(
                    self.name,
                    self.topic, 
                    self.rate)
                    


article1= Knowledge(name="Donald Trump", topic="Prime Ministers" , rate= 6 )
print(article1)

article2= Knowledge(name="Little Mix", topic="Bands" , rate= 10 )
print(article2)

article3= Knowledge(name="The Notebook", topic="Movies" , rate= 8 )
print(article3)

article4=Knowledge(name= "rainbow", topic="weather", rate= 9 )
print(article4)


    
    






	




