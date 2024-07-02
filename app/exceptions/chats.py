import json
from dataclasses import dataclass

from exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class BaseWebException(ApplicationException):
    status_code: int
    response_content: str

    @property
    def response_json(self) -> dict:
        return json.loads(self.response_content)

    @property
    def error_text(self) -> dict:
        return self.response_json.get('detail', {}).get('error', '')


@dataclass(frozen=True, eq=False)
class ChatListRequestError(BaseWebException):
    @property
    def message(self):
        return "Couldn't get the chat list"


@dataclass(frozen=True, eq=False)
class ChatListenerListRequestError(BaseWebException):
    @property
    def message(self):
        return "Couldn't get all the chat listeners"


@dataclass(frozen=True, eq=False)
class ChatListenerAddRequestError(BaseWebException):
    @property
    def message(self):
        return "Couldn't add listener to chat"


@dataclass(frozen=True, eq=False)
class ChatInfoRequestError(BaseWebException):
    @property
    def message(self):
        return "Can't get information about chat"
