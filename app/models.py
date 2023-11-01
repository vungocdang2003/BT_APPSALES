from sqlalchemy import  Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
import app
from app import db, app

class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key= True, autoincrement = True)
    name = Column(String(50), nullable= False, unique= True)
    products = relationship('product', backref='category', lazy= True)

class Products(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(200))
    category_ID = Column(Integer, ForeignKey(Category.id), nullable= False)

if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name = 'Mobile')
        # c2 = Category(name = 'Tablet')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        p1 = Products(name='Iphone13', price= 2000000,
                      image ='https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-vang-thumb-600x600.jpg',
                      category_ID = 1)
        p2 = Products(name ='Samsung A20',price= 2200000,
                      image ='https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-vang-thumb-600x600.jpg',
                      category_ID = 1)
        p3 = Products(name='Iphone13', price=2000000,
                      image='https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-vang-thumb-600x600.jpg',
                      category_ID=1)
        p4 = Products(name='Samsung A20', price=2200000,
                      image='https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-vang-thumb-600x600.jpg',
                      category_ID=1)
        db.session.add_all([p1,p2,p3,p4])
        db.session.commit()
        # db.create_all()