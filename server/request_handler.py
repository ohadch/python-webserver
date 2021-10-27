class RequestHandler:

    def __init__(self, endpoint: str, action: callable):
        self.endpoint = endpoint
        self.action = action

    def handle(self):
        return self.action()
