from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/")
async def base_get_route():
    return {"message": "hello world"}

@app.post("/")
async def post():
    return {"message": "Hello from the post route"}

@app.put("/")
async def put():
    return {"message": "Hello from PUT route"}

@app.get("/items")
async def list_items():
    return {"message": "List items routes"}

@app.get("/items/{item_id}")
async def get_items(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me")
async def get_current_user():
    return {"Message": "this is the current user"}

@app.get("/users/{user_id}")
async def get_user(user_id):
    return {"user_id": user_id}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}
    
    if food_name == FoodEnum.fruits:
        return {"food_name": food_name, "message": "you are still healthy, but like sweet things"}
    return {"food_name": food_name, "message": "i like chocolate milk"}