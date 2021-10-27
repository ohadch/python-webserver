from server import Server, RequestHandler, Response


def hello_world() -> Response:
    return {"code": 200, "message": "Hello world!"}


app = Server([
    RequestHandler("GET", "/test", hello_world)
])

if __name__ == '__main__':
    app.listen(8080)
