# 不可以使用GET请求发送请求体
# 发送请求体的方法有POST、PUT、PATCH、DELETE等

# 导入fastapi
from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel
from enum import Enum

# 创建FastAPI的实例
app = FastAPI()

class Gender(str, Enum):
    male = 'male'
    female = 'female'


class UserModel(BaseModel):
    username: str
    description: Optional[str] = 'default'
    gender: Gender


# 创建一个根路径的POST请求处理函数
@app.post("/users")
async def creat_users(user_model: UserModel): 
    print(user_model.username)
    user_dict = user_model.model_dump()  # 将模型转换为字典
    
    return user_dict

# 创建一个根路径的PUT请求处理函数
@app.put("/users/{user_id}")
async def update_users(user_id: int, user_model: UserModel): 
    print(user_model.username)
    user_dict = user_model.model_dump()  # 将模型转换为字典
    user_dict.update({"id": user_id})
    
    return user_dict

                
if __name__ == "__main__":
    uvicorn.run("04_请求体:app", reload=True)