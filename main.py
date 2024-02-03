from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return { "name":"Vikash" }


users=[
    {
        "name":"abc",
        "age":23
    },
    {
        "name":"def",
        "age":"25"
    }
]

@app.get("/getUser/{userId}")
def getUser(userId:int):
    return users[userId]


@app.get("/getByName")
def getByName(name:str):
    for user in users:
        if user['name']==name:
            return user