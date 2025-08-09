# 多个请求体参数
# 不可以使用GET请求发送请求体
# 发送请求体的方法有POST、PUT、PATCH、DELETE等

# 导入fastapi
from fastapi import FastAPI, Path, Query, Body
import uvicorn
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum
from typing import List

# 创建FastAPI的实例
app = FastAPI()

class Address(BaseModel):
    address: str
    postcode: str


class User(BaseModel):
    username: str = Field(..., min_length= 3)
    description: Optional[str] = 'default'
    address: Address

class Item(BaseModel):
    name: str
    length: int
    features: List[str]

@app.put("/carts/{cart_id}")
async def update_cart(cart_id: int, user: User, item: Item, count: int = Body(..., ge = 1)): 
    print(user.username)
    print(item.name)
    result_dict = {
        'cart_id': cart_id,
        'username': user.username,
        'itemname': item.name,
        'count': count
    }
    
    return result_dict



                
if __name__ == "__main__":
    uvicorn.run("06_深入请求体:app", reload=True)