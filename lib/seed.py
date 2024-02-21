from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review


engine = create_engine('sqlite:///restaurants.db')
Base.metadata.bind = engine


Session = sessionmaker(bind=engine)
session = Session()


Java = Restaurant(name='Java', price=3)
CJs = Restaurant(name='CJs', price=4)
The_law_steakhouse = Restaurant(name='The_law_steakhouse', price=5)

session.add_all([Java, CJs, The_law_steakhouse])
session.commit()


Bm = Customer(first_name='Big', last_name='Mom')
Kb = Customer(first_name='Kaido', last_name='Beast')
Rjo = Customer(first_name='Robert', last_name='Oppenheimer')

session.add_all([Bm,Kb ,Rjo ])
session.commit()


review1 = Review(star_rating=4, restaurant=Java, customer=Bm)
review2 = Review(star_rating=5, restaurant=CJs, customer=Kb)
review3 = Review(star_rating=3, restaurant = The_law_steakhouse, customer=Rjo)

session.add_all([review1, review2, review3])
session.commit


session.close()