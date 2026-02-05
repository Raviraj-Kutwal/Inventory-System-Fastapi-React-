from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import SessionLocal ,engine
import database_models
from sqlalchemy.orm import Session  
from pydantic import BaseModel


database_models.Base.metadata.create_all(bind=engine)    

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
    
)
   
    
products=[
    Product(id=1,name="phone",price=6890,description="Cheap Phone",quantaity=1)
    ,Product(id=2,name="PS5",price=36890,description="Gaming Console",quantaity=2)
    ,Product(id=3,name="Tablet",price=15000,description="mid-range Tablet",quantaity=3)
    ,Product(id=4,name="Trimmer",price=890,description="Hair Trimmer",quantaity=1)
]
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
    db.close()
    
def init_db():
    db=SessionLocal()
    
    count=db.query(database_models.Product).count()
    
    if count==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
            
        db.commit()
init_db()
    

# @app.get("/")
# def greet():
#     return "Welcome"




@app.get("/products/")
def get_all_products(db:Session=Depends(get_db)):
    db_products=db.query(database_models.Product).all()
    return db_products



    

@app.get("/products/{product_id}")
def get_product(product_id:int,db:Session=Depends(get_db)):
    db_products=db.query(database_models.Product).filter(database_models.Product.id==product_id).first()
    if db_products:
        return db_products
      
    return {"Error":"Product not found"}


@app.post("/products/")
def add_product(product:Product,db:Session=Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product


@app.put("/products/{product_id}")
def update_product(product_id:int,product:Product,db:Session=Depends(get_db)):
    db_products=db.query(database_models.Product).filter(database_models.Product.id==product_id).first()
    if db_products:
        db_products.name=product.name
        db_products.price=product.price
        db_products.description=product.description
        db_products.quantaity=product.quantaity
        db.commit()
        return "Product updated"
    return {"Error":"Product not found"}


@app.delete("/products/{product_id}")
def delete_product(product_id:int,db:Session=Depends(get_db)):
    db_products=db.query(database_models.Product).filter(database_models.Product.id==product_id).first()
    if db_products:
        db.delete(db_products)
        db.commit()
        return "Product deleted"
    else:
        return {"Error":"Product not found"}
    
       




    





    
