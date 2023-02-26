from typing import Optional

from incendium.helper.types import AnyStr, InnerException
from java.lang import Throwable

class ApplicationError(Exception):
    cause: Optional[Throwable]
    inner_exception: InnerException
    message: AnyStr
    def __init__(
        self,
        message: AnyStr,
        inner_exception: InnerException = ...,
        cause: Optional[Throwable] = ...,
    ) -> None: ...

class TagError(Exception):
    message: AnyStr
    def __init__(self, message: AnyStr) -> None: ...
