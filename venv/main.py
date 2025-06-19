from fastapi import FastAPI

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
