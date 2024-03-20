from fastapi import FastAPI
import uvicorn
import model
from db import engine
from routes import router

app = FastAPI() 

model.Base.metadata.create_all(bind=engine)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=8001)
