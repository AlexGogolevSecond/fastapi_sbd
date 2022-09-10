from fastapi import FastAPI
import json
import pandas as pd
import uvicorn
from date_request_model import User


app = FastAPI()


@app.get("/")
async def root():
    return "Phonebook"

 
@app.post("/add-user")
async def add_user(parameters: User):
    # Считываем/создаём телефонный справочник
    try:
        df_phonebook = pd.read_csv('db.csv')
    except:
        df_phonebook = pd.DataFrame(columns=['Firstname', 'Lastname', 'Phone number', 'Age'])
        df_phonebook['Phone number'] = df_phonebook['Phone number'].astype(str)

    print(type(parameters))
    user_dict = {}
    user_dict['Firstname'] = parameters.firstname
    user_dict['Lastname'] = parameters.lastname
    user_dict['Phone number'] = parameters.phone_number

    user_dict['Age'] = parameters.age if parameters.age else 'None'

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
    # return f'{lastname} 89021112223 55'
    try:
        df_phonebook = pd.read_csv('db.csv')
        # df_phonebook['Phone number'] = df_phonebook['Phone number'].astype(str)
    except:
        df_phonebook = pd.DataFrame(columns=['Firstname', 'Lastname', 'Phone number', 'Age'])

    df_temp = df_phonebook[df_phonebook['Lastname'] == lastname]
    if df_temp.empty:
        return ' There is not such user'

    print(dict(df_temp.iloc[0]))
    value = json.dumps(dict({'Phone number': df_temp.iloc[0]['Phone number']}))
    return value

# if __name__ == '__main__':
#     uvicorn.run('main:app')
