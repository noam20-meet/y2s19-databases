from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name, topic, rate):
	new_article=Knowledge(name=name, topic=topic, rate=rate)
	session.add(new_article)
	session.commit()


def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles
	

def query_article_by_topic(topic):
	article = session.query(Knowledge).filter_by(
		topic=topic).first()
	return article
	

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(
		topic=topic).delete()
	session.commit()
delete_article_by_topic("Bands")

	

def delete_all_articles():
	pass

def edit_article_rating():
	pass




