from server import Server, RequestHandler


def hello_world():
    return "Hello world!"


app = Server([
    RequestHandler("/", hello_world)
])

if __name__ == '__main__':
    app.listen(8080)
