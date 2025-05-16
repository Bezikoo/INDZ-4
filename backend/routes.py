from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from backend.models import RegistrationData

router = APIRouter()

# Тимчасова база даних
fake_db = []

@router.post("/register")
async def register_user(data: RegistrationData):
    if any(user['email'] == data.email for user in fake_db):
        raise HTTPException(status_code=400, detail="Email already registered")
    fake_db.append(data.dict())
    return {"message": "Registration successful"}

@router.get("/users")
async def get_users():
    return fake_db

@router.get("/user/{email}")
async def get_user(email: str):
    user = next((u for u in fake_db if u["email"] == email), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/user/{email}")
async def delete_user(email: str):
    global fake_db
    new_db = [u for u in fake_db if u["email"] != email]
    if len(new_db) == len(fake_db):
        raise HTTPException(status_code=404, detail="User not found")
    fake_db = new_db
    return {"message": "User deleted successfully"}

@router.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})
