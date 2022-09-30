from typing import Optional

from incendium.helper.types import InnerException, String
from java.lang import Throwable

class ApplicationError(Exception):
    cause: Optional[Throwable]
    inner_exception: InnerException
    message: String
    def __init__(
        self,
        message: String,
        inner_exception: InnerException = ...,
        cause: Optional[Throwable] = ...,
    ) -> None: ...

class TagError(Exception):
    message: String
    def __init__(self, message: String) -> None: ...
