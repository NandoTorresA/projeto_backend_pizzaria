from fastapi import FastAPI # uvicorn main:app --reload
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer


load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACESS_TOKEN_EXPIRES_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRES_MINUTES'))

app = FastAPI()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_schema = OAuth2PasswordBearer(tokenUrl='/auth/login-form')


from order_routes import order_router
from auth_routes import auth_router

app.include_router(auth_router)
app.include_router(order_router)