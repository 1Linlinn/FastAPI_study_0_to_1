# 导入fastapi
from fastapi import FastAPI
import uvicorn
from enum import Enum


# 创建FastAPI的实例
app = FastAPI()

# 定义一个枚举类
class Gender(str, Enum):
    male = 'male'
    female = 'female'
    
    
# 创建一个根路径的GET请求处理函数
# 顺序很重要，小范围在前，大范围在后
@app.get("/users/current")
async def get_current_user():
    return {"user": f"This is current user"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user": f"This is user {user_id}"}

@app.get("/students/{gender}")
async def get_user(gender: Gender):
    return {"student": f"This is a {gender.value} student"}


if __name__ == "__main__":
    uvicorn.run("02_路径参数:app", reload=True)