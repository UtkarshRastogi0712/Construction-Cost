from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from server.models.user import UserSchema
from server.routes.project import router as ProjectRouter
from server.helper.login import *

app = FastAPI()
app.include_router(ProjectRouter, tags=["Project"], prefix="/project")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/", tags=["Root"])
async def read_root(token: str = Depends(oauth2_scheme)):
    return {"message":"Welcome to Constuction Cost estimator", "token": token}

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserSchema(**user_dict)
    hashed_password=fake_hashed_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/user")
async def read_user(current_user: UserSchema = Depends(get_current_user)):
    return current_user