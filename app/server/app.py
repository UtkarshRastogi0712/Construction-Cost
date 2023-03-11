from fastapi import FastAPI
from server.routes.project import router as ProjectRouter

app = FastAPI()
app.include_router(ProjectRouter, tags=["Project"], prefix="/project")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message":"Welcome to Constuction Cost estimator"}