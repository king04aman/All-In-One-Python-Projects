from sqlalchemy.orm import sessionmaker
from models import JournalEntry, Base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///journal.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_entry(user_id, mood, content, tags):
    entry = JournalEntry(user_id=user_id, mood=mood, content=content, tags=tags)
    session.add(entry)
    session.commit()

def search_entries(user_id, search_term=None, date=None):
    query = session.query(JournalEntry).filter(JournalEntry.user_id == user_id)
    if search_term:
        query = query.filter(JournalEntry.content.contains(search_term))
    if date:
        query = query.filter(JournalEntry.date == date)
    return query.all()
