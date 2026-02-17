from fastapi  import FastAPI
from routes import user
from routers import auth

app.include_router(auth.router)
@app.get("/")
def read_root():
    return{"message":"wellcom my heartiya"}
