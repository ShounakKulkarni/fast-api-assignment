from fastapi import FastAPI, APIRouter, HTTPException
from configurations import collection
from database.models import UserData
from database.schema import *
from bson.objectid import ObjectId

app = FastAPI()
router = APIRouter()

@router.get("/")
async def get_all_users():
    data = collection.find()
    return all_users(data)

@router.get("/{user_id}")
async def get_single_user(user_id: str):
    data = collection.find_one({"_id": ObjectId(user_id)})
    return individual_user(data)

@router.post("/")
async def create_user(user: UserData):
    try:
        resp = collection.insert_one(dict(user))
        return {"status_code":200, "id": str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"some error occured {e}")
    
@router.put("/{user_id}")
async def update_user(user_id: str, updated_user: UserData):
    try:
        id = ObjectId(user_id)
        existing_user = collection.find_one({"_id": id})

        if not existing_user:
            return HTTPException(status_code=404, detail=f"User does not exist")
        
        resp = collection.update_one({"_id": id}, {"$set": dict(updated_user)})
        return {"status_code": 200, "message": "user updated successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"some error occured {e}")
    
@router.delete("/{user_id}")
async def delete_user(user_id: str):
    try:
        id = ObjectId(user_id)
        existing_user = collection.find_one_and_delete({"_id": id})

        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")
        
        return {"status_code": 200, "message": "user deleted successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"some error occured {e}")
    

app.include_router(router)
