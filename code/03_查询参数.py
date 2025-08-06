# 导入fastapi
from fastapi import FastAPI
import uvicorn
from typing import Optional


# 创建FastAPI的实例
app = FastAPI()


# 创建一个根路径的GET请求处理函数
@app.get("/users")
async def get_users(page_index: int , page_size: Optional[int] = 30): # 设置默认值
    return {"page_info": f"index is {page_index}, size is {page_size}"}

# 没有在路径参数里面定义都是查询参数
@app.get("/users/{user_id}/friends")
async def get_user_friends(user_id: int, page_index: int, page_size: Optional[int] = 10):
    return {"user_id": user_id, "friends": f"Page {page_index} with size {page_size}"}


                
if __name__ == "__main__":
    uvicorn.run("03_查询参数:app", reload=True)