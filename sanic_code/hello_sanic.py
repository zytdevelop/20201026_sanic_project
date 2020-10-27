from sanic import Sanic
from sanic.response import text, json, html, file
from sanic_cors import CORS

# 引入 sanic 包

# 创建一个webapp,创建主程序
app = Sanic(__name__)

# CORS()函数用来解决跨域问题
CORS(app)


# 接收请求的路由
@app.route("/")
def func1(req):
    return text("Hi, this is sanic")


# req.args.get() 获取url请求中的数据字典
@app.route("/login")
def func2(req):
    uname = req.args.get("username")
    pwd = req.args.get("password")
    if uname == 'zyt' and pwd == '9999':
        return text("200 OK!Success!")
    else:
        return text("404 NOT OK!FAIL!")


# path 参数
# /abc/123456

# 限制参数类型用冒号  --> <id:int>
@app.route("/abc/<id:int>")
def func3(req, id):
    print(id)
    return text("123")


# 改变请求方式，上述函数得到的请求都是GET请求
# 下面学习post请求
# req.args获取的是url字符串中的请求参数,问号传参
# req.form获取的是post请求中的表单数据,表单数据-->sanic 表单数据中列表经过封装, 并不是python自带的列表类
@app.route("/ddd", methods=["POST"])
def func4(req):
    print("this is a POST request!")
    print(req.args)
    print(type(req.form))
    username = req.form.get("username")
    print(username)
    return text("I response for a POST request!")


# 返回值
# text：返回文本
# json：返回json
# html：返回html页面
@app.route("/return")
def func5(req):
    if req.args.get("type") == 'json':
        return json({'age': 1, 'sex': 0})
    elif req.args.get("type") == 'html':
        return html({'a': 1, })
    else:
        return file('/templates/index.html')


if __name__ == '__main__':
    app.run(debug=True, port=9527)
