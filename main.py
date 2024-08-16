from fastapi import Body,FastAPI,Path,File,UploadFile,Form, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from starlette.exceptions import HTTPException as StarletteHTTPException
from enum import Enum
from pydantic import BaseModel, HttpUrl
from typing import Annotated



app = FastAPI()

# @app.get("/")
# async def base_get_route():
#     return {"message": "hello world"}

# @app.post("/")
# async def post():
#     return {"message": "Hello from the post route"}

# @app.put("/")
# async def put():
#     return {"message": "Hello from PUT route"}


# @app.get("/users/me")
# async def get_current_user():
#     return {"Message": "this is the current user"}

# @app.get("/users/{user_id}")
# async def get_user(user_id):
#     return {"user_id": user_id}

# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     dairy = "dairy"

# @app.get("/foods/{food_name}")
# async def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {"food_name": food_name, "message": "you are healthy"}
    
#     if food_name == FoodEnum.fruits:
#         return {"food_name": food_name, "message": "you are still healthy, but like sweet things"}
#     return {"food_name": food_name, "message": "i like chocolate milk"}


# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Jaz"}]

# # Query Parameters
# # @app.get("/items")
# # async def list_items(skip: int = 0, limit: int = 10):
# #     return fake_items_db[skip : skip + limit]

# # Optional Query Parameters 

# @app.get("/items/{item_id}")
# async def get_item(item_id: str,sample_query_param: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "sample_query_param": sample_query_param}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc congue."
#             }
#         )
    
#     return item

# @app.get("/users/{user_id}/items/{item_id}")
# async def get_user_item(
#     user_id: int, item_id: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc congue."
#             }
#         )
    
#     return item

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.post("/items")
# async def create_item(item: Item) -> Item:
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id" : item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result


# @app.get("/items")
# async def read_items(q: str
#                      | None = Query(
#                          None,
#                          min_length=3,
#                          max_length=10,
#                          title="Sample query string",
#                          description="This is a sample query string",
#                          alias="item-query"
#                      )):   ##q: str = Query("fixedquery",min_length =3, max_length = 10)  ## for required condition Query(...,min_length =3, max_length = 10)
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items_hidden")
# async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     return {"hidden_query": "Not found"}


# @app.get("/items_validation/{item_id}")
# async def read_items_validations(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", 
#     gt=10, lt=100), 
#     q: str="hekko",
#     size: float = Query(..., gt=0, lt=7.6)
# ):
#     results = {"item_id": item_id, "size": size}
#     if q:
#         results.update({'q': q})
#     return results


### Body - Multiple Parameters

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# class User(BaseModel):
#     username: str 
#     full_name: str | None = None

# # class Importance(BaseModel):
# #     importance: int

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", gt=0, lt=150),
#     q: str | None = None,
#     item: Item | None = None,
#     user: User,
#     importance: Annotated[int, Body()]
# ):
#     #results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     elif item:
#         results.update({"item": item})
#     elif user:
#         results.update({"user": user})
#     elif importance:
#         results.update({"importance", importance})
#     return results


### Body  - Fields
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         None, title="The description of the item", max_length=300
#     )
#     price: float = Field(..., gt=0, description="The price must be greater than zero")
#     tax: float | None = None
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results

### Nested Models
# class Image(BaseModel):
#     url: HttpUrl
#     name: str

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None
#     tags: set[str] = []
#     image: list[Image] | None = None

# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     items: list[Item]

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#    results = {"item_id": item_id, "item": item}
#    return results 

# @app.post("/offers")
# async def create_offer(offer: Offer = Body(..., embed=True)):
#     return offer

# @app.post("/images/multiple")
# async def create_multiple_images(images: list[Image]):
#     return images

# @app.post("/blah")
# async def create_some_blahs(blahs: dict[int, float]):
#     return blahs

### 10. Declare Request Example Data

### 11. Extra data types

### 12. Cookie and Header Parameter

### 13. Response Model  -- Go through again

### 14. Extra Models

### 15. Respose Status Codes

### 16. Form Fields


# @app.post("/login")
# async def login(username: str = Form(...), password: str = Form(...)):
#     print("password", password)
#     return {'username': username}

# class User(BaseModel):
#     username: str
#     password: str
#
# @app.post("/login-json/")
# async def login_json(user: User):
#     return  user

# Using as BOdy
# @app.post("/login-json/")
# async def login_json(username: str = Body(...), password: str = Body(...)):
#     print("password", password)
#     return {'username': username}

### 17. Request Files

# @app.post("/files/")
# async def create_file(
#         files: list[bytes] = File(..., description="A file read as bytes")
# ):
#     return {"file_size": [len(file) for file in files]}


# @app.post("/uploadfile/")
# async def create_upload_file(
#     files: list[UploadFile] = File(..., description="A file read as Uploadfile")
#     ):
#     return {"filename": [file.filename for file in files]}

### Request forms and files

# @app.post("/files/")
# async def create_file(file: bytes=File(...), fileb: UploadFile = File(...), token: str = Form(...), hello: str = Body(...)):
#     return {
#         "file_size": len(file),
#         "token": token,
#         "fileb_content_type": fileb.content_type,
#         "hello": hello,
#     }

### Handling Errors
# items = {"foo": "The Foo Wrestlers"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="Item not Found",headers={"X-Error": "There goes my erro"})
#     return {"item": items[item_id]}

# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name
        
# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418, 
#         content={"message": f"Oops! {exc.name} did something, There goes a rainbow"},

#     )

# @app.get("/unicorns/{name}")
# async def read_unicorns(name: str):
#     if name == "yolo":
#         raise UnicornException(name=name)
#     return {"unicorn_name": name}


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)

# @app.get("/validation_items/{item_id}")
# async def read_validation_items(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
#     return {"item_id": item_id}

# @app.exception_handler(StarletteHTTPException)
# async def custom_htt_exception_handler(request, exc):
#     print(f"OMG! An HTTP error!: {repr(exc)}")
#     return await http_exception_handler(request, exc)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     print(f"OMG! The Client sent invalid data!: {exc}")
#     return await request_validation_exception_handler(request, exc)

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3")
#     return {"item_id": item_id}

### Path Operation Configuration
