from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import SessionLocal ,engine
import database_models as database_models
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
    try:
        count=db.query(database_models.Product).count()
        
        if count==0:
            for product in products:
                db.add(database_models.Product(**product.model_dump()))
                
            db.commit()
    finally:
        db.close()
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
    # Add product
    new_product = database_models.Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    
    # Log history
    history = database_models.ItemHistory(
        product_id=new_product.id,
        name=new_product.name,
        action="ADDED"
    )
    db.add(history)
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
        # Log history before delete
        history = database_models.ItemHistory(
            product_id=product_id,
            name=db_products.name,
            action="DELETED"
        )
        db.add(history)
        
        db.delete(db_products)
        db.commit()
        return "Product deleted"
    else:
        return {"Error":"Product not found"}

@app.get("/dashboard/stats")
def get_dashboard_stats(db:Session=Depends(get_db)):
    from sqlalchemy import func
    
    # 1. Total Quantity
    total_qty = db.query(func.sum(database_models.Product.quantaity)).scalar() or 0
    
    # 2. Activity Log (Grouped by Date)
    # We will fetch all history and aggregate in python for simplicity in this small app
    history_records = db.query(database_models.ItemHistory).all()
    
    # Process history
    activity_map = {}
    
    for record in history_records:
        date_str = record.timestamp.strftime("%Y-%m-%d")
        if date_str not in activity_map:
            activity_map[date_str] = {"date": date_str, "added": 0, "deleted": 0}
        
        if record.action == "ADDED":
            activity_map[date_str]["added"] += 1
        elif record.action == "DELETED":
            activity_map[date_str]["deleted"] += 1
            
    # Convert map to sorted list
    activity_list = sorted(activity_map.values(), key=lambda x: x["date"])
    
    return {
        "total_quantity": total_qty,
        "activity": activity_list
    }

       




    





    
