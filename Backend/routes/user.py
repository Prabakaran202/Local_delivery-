from fastapi import APIRouter, HTTPException
from schemas.user import UserLogin

router = APIRouter()

fake_user = {
    "email": "test@gmail.com",
    "password": "1234"
}

@router.post("/login")
def login(user: UserLogin):
    if user.email != fake_user["email"] or user.password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": "Login successful"}
