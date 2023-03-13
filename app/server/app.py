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

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=UserSchema)
async def read_user(current_user: UserSchema = Depends(get_current_user)):
    return current_user