from fastapi import FastAPI
import json
import pandas as pd
 
app = FastAPI()


@app.get("/")
async def root():
    return "Phonebook"

 
@app.post("/add-user")
async def add_user(firstname: str, lastname: str, phone_number: str, age: int | None = None):
    # Считываем/создаём телефонный справочник
    try:
        df_phonebook = pd.read_csv('db.csv')
    except:
        df_phonebook = pd.DataFrame(columns=['Firstname', 'Lastname', 'Phone number', 'Age'])
        df_phonebook['Phone number'] = df_phonebook['Phone number'].astype(str)

    user_dict = {}
    user_dict['Firstname'] = firstname
    user_dict['Lastname'] = lastname
    user_dict['Phone number'] = phone_number

    user_dict['Age'] = age if age else None

    print(f'user_dict: {user_dict}')
    df_temp = pd.DataFrame([user_dict])
    print(f'df_phonebook: {df_phonebook}')
    print(f'df_temp: {df_temp}')
    df_phonebook = pd.concat([df_phonebook, df_temp])
    df_phonebook.to_csv('db.csv')

    # print(f'firstname: {firstname}')
    # print(f'lastname: {lastname}')
    # print(f'phone_number: {phone_number}')
    #
    # if age:
    #     print(f'age: {age}')

    return 'user is added'

 
@app.get("/get-user")
async def get_user(lastname: str):
    return f'{lastname} 89021112223 55'
