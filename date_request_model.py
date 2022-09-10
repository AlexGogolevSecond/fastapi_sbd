from pydantic import BaseModel, validator, validate_model


class User(BaseModel):
    firstname: str
    lastname: str
    phone_number: str
    age: int | None = 0

    @validator('phone_number')
    def parse_phone_number(cls, phone_number: str):
        return f'Phone: {phone_number} XXX'
