from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
async def root():
    return "Phonebook"
 
@app.post("/add-user")
async def add_user(firstname: str, lastname: str, phone_number: str, age: int | None = None):
    print(f'firstname: {firstname}')
    print(f'lastname: {lastname}')
    print(f'phone_number: {phone_number}')
 
    if age:
        print(f'age: {age}')
 
    return 'user is added'
 
@app.get("/get-user")
async def get_user(lastname: str):
    return f'{lastname} 89021112223 55'
