from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class ApplicationException(BaseException):
    @property
    def message(self):
        return "Application Error"
