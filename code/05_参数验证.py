# 参数验证的工具类
# 路径参数：fastapi.Path
# 查询参数：fastapi.Query

# 导入fastapi
from fastapi import FastAPI, Path, Query
import uvicorn
from enum import Enum


# 创建FastAPI的实例
app = FastAPI()

# 定义一个枚举类
class Gender(str, Enum):
    male = 'male'
    female = 'female'

@app.get("/users")
async def get_users(page_index: int = Query(1, title='Page Index', ge = 1, le = 1000)):
    return {"user": f"Index: {page_index}"}
   
# 验证最大最小值 
@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(..., title='user ID', ge = 0, le = 1000)):
    return {"user": f"This is user {user_id}"}


@app.get("/books/{book_name}")
async def get_book(book_name: str = Path(..., title='Book Name', min_length=3, max_length=10),):
    return {"book": f"This is a book for {book_name}"}

# 也可以使用正则表达式进行参数验证
@app.get("/items/{item_no}")
async def get_item(item_no: str = Path(..., title='Item No', regex='^[a|b|c]-[\\d]*$')):
    return {"item": f"This is a book for {item_no}"}



if __name__ == "__main__":
    uvicorn.run("05_参数验证:app", reload=True)