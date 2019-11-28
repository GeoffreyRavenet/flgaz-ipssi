import connect_db
import models

def select_all():
    for p in connect_db.s.query(models.Tweet).all():
        print(p)

# Insertion, équivalent de "INSERT INTO"
def insert_tweet():
    form = models.Tweet(content="depuis SQLAlchemy", 
            delay="message",
            date_creation=False, 
            is_temporary=False,
            categorie = "")
    connect_db.s.add(form)
    connect_db.s.commit()

