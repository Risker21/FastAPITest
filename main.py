from fastapi import FastAPI

from Emp.test import emp

app = FastAPI()


app.include_router(emp)




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
