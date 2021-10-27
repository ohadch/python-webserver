from typing import Literal, TypedDict


class Response(TypedDict):
    code: int
    message: str


TYPE_REQUEST_METHOD = Literal["GET", "POST", "PUT", "DELETE"]