from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app=FastAPI()

class TestModel(BaseModel):
    id:int
    topic:str
    content:str

#without database storing it in test data
test_data:List[TestModel]=[]

@app.get("/")
def read_root():
    return{"Message":"Welcome to your first project"}

@app.get("/test")
def get_data():
    return test_data

@app.post("/test")
def create_data(new_data: TestModel):
    test_data.append(new_data)

@app.put("/test/{data_id}")
def update_data(data_id:int, updated_data: TestModel):
    for index, data in enumerate(test_data):
        if data.id==data_id:
         test_data[index]=updated_data
         return {"message":"Data updated successfully", "data":updated_data}
    return{"error":"Data not found"}

@app.delete("/test/{data_id}")
def delete_data(data_id:int):
    for index, data in enumerate(test_data):
        if data.id==data_id:
            deleted=test_data.pop(index)
            return deleted
    return("Data not found")

# Getting a single value from id
@app.get("/test/{data_id}")
def show(data_id:int):
    for data in test_data:
     if data_id==data_id:
        return data
    return{"error":"Data not found"}

