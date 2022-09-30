from typing import Optional

from incendium.helper.types import String

CURSOR_DEFAULT: int
CURSOR_CROSSHAIR: int
CURSOR_TEXT: int
CURSOR_WAIT: int
CURSOR_SW_RESIZE: int
CURSOR_SE_RESIZE: int
CURSOR_NW_RESIZE: int
CURSOR_NE_RESIZE: int
CURSOR_N_RESIZE: int
CURSOR_S_RESIZE: int
CURSOR_W_RESIZE: int
CURSOR_E_RESIZE: int
CURSOR_HAND: int
CURSOR_MOVE: int

def confirm(
    message: String, title: String = ..., show_cancel: bool = ...
) -> Optional[bool]: ...
def error(
    message: String, title: String = ..., detail: Optional[String] = ...
) -> None: ...
def info(
    message: String, title: String = ..., detail: Optional[String] = ...
) -> None: ...
def input(message: String, title: String = ...) -> Optional[String]: ...
def warning(
    message: String, title: String = ..., detail: Optional[String] = ...
) -> None: ...
