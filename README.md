# FastAPI_study_0_to_1
参考B站UP主[跟着峰哥学编程](https://space.bilibili.com/3461574561892826) 的[FastAPI教学视频](https://space.bilibili.com/3461574561892826/lists/2056242?type=season)

## Day 01 第一个Restful API
### 输出hello world
```python
# 导入fastapi
from fastapi import FastAPI
import uvicorn

# 创建FastAPI的实例
app = FastAPI()

# 创建一个根路径的GET请求处理函数
@app.get("/helloworld")
async def hello_world():
    return {"message": "Hello, World!"}



# 运行的两种方式
# # 1. 在终端中运行以下命令
# cmd终端先进入对应的文件夹再运行命令, 注意app前面是py文件名
# uvicorn 01_Hello_FastAPI:app --reload

# # 2. 在代码中添加以下代码
if __name__ == "__main__":
    uvicorn.run("01_Hello_FastAPI:app", reload=True)
```

### 运行的两种方式
1. 在终端中运行以下命令
   cmd终端先进入对应的文件夹再运行命令, 注意app前面是py文件名
   ```bash
   uvicorn 01_Hello_FastAPI:app --reload
   ```
2. 在代码中添加以下代码
   ```python
   if __name__ == "__main__":
       uvicorn.run("01_Hello_FastAPI:app", reload=True)
   ```  

### 查看现有的请求函数的参数与响应
运行后在浏览器中访问 http://127.0.0.1:8000/docs
![1754408182972](image/README/1754408182972.png)

## Day 02 路径参数和查询参数
### 路径参数
在路径中定义参数，参数会作为函数的参数传入
函数的顺序很重要，小范围在前，大范围在后，默认使用第一个，限制user_id为int类型
![1754489907100](image/README/1754489907100.png)

对于枚举类型的路径参数，通过创建枚举类实现
```python
# 定义一个枚举类
from enum import Enum
class Gender(str, Enum):
    male = 'male'
    female = 'female'

@app.get("/students/{gender}")
async def get_user(gender: Gender):
    return {"student": f"This is a {gender.value} student"}
```

### 查询参数
查询参数是URL中`?`后面的参数，可以有多个，多个参数之间用`&`连接
把查询参数放在请求函数的参数中即可，FastAPI会自动识别
没有在路径参数里面定义都是查询参数
![1754491749962](image/README/1754491749962.png)

代码示例
```python
@app.get("/users")
async def get_users(page_index: int , page_size: int ):
    # page_index: 页码
    # page_size: 每页显示的条数
    return {"page_info": f"index is {page_index}, size is {page_size}"}
```

### 可选查询参数
通过`typing`模块的`Optional`类型实现可选查询参数默认值；

```python
from typing import Optional
@app.get("/users")
async def get_users(page_index: int , page_size: Optional[int] = 30):
    # page_index: 页码
    # page_size: 每页显示的条数，默认值为30
    return {"page_info": f"index is {page_index}, size is {page_size}"}
```

