from os import name
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name:str
    price:float
    is_active: bool = False


app = FastAPI()

@app.get("/")
def start():
    return {"Hello": "World"}

@app.get("/item")
def item():
    return "item is here"

@app.get("/item/{id}")
def item(id:int):
    return f"Item {id} is here"

@app.get("/user")
def user():
    return "user is here"

@app.get("/user/{username}")
def user(username:str):
    return f"Username is: {username}"


@app.get("/products/{id}")
def product(id: int, rating: float, inStock: bool = True):
    return {
        "id": id,
        "inStock": inStock,
        "rating": rating
    }


@app.post('/add-item')
def addItem(item : Item):
    return {
        "name": item.name,
        "price": item.price,
        "is_active": item.is_active
    }