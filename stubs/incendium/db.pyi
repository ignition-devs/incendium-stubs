from types import TracebackType
from typing import Any, List, Optional, Tuple, Type, Union

from com.inductiveautomation.ignition.common import BasicDataset
from incendium.helper.types import DictIntStringAny, String

class DisposableConnection:
    database: String
    retries: int
    def __init__(self, database: String, retries: int = ...) -> None: ...
    def __enter__(self) -> DisposableConnection: ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...
    @property
    def status(self) -> String: ...

class Param:
    def __init__(
        self,
        name_or_index: Union[int, String],
        type_code: int,
        value: Optional[Any] = ...,
    ) -> None: ...
    @property
    def name_or_index(self) -> Union[int, String]: ...
    @property
    def type_code(self) -> int: ...
    @property
    def value(self) -> Optional[Any]: ...

class InParam(Param):
    def __init__(
        self, name_or_index: Union[int, String], type_code: int, value: Any
    ) -> None: ...

class OutParam(Param):
    def __init__(self, name_or_index: Union[int, String], type_code: int) -> None: ...

def check(
    stored_procedure: String,
    database: String = ...,
    params: Optional[List[InParam]] = ...,
) -> Optional[bool]: ...
def execute_non_query(
    stored_procedure: String,
    database: String = ...,
    transaction: Optional[String] = ...,
    params: Optional[List[InParam]] = ...,
) -> int: ...
def get_data(
    stored_procedure: String,
    database: String = ...,
    params: Optional[List[InParam]] = ...,
) -> BasicDataset: ...
def get_output_params(
    stored_procedure: String,
    output: List[OutParam],
    database: String = ...,
    transaction: Optional[String] = ...,
    params: Optional[List[InParam]] = ...,
) -> DictIntStringAny: ...
def get_return_value(
    stored_procedure: String,
    return_type_code: int,
    database: String = ...,
    transaction: Optional[String] = ...,
    params: Optional[List[InParam]] = ...,
) -> Optional[int]: ...
def o_execute_non_query(
    stored_procedure: String,
    out_params: List[OutParam],
    database: String = ...,
    transaction: Optional[String] = ...,
    in_params: Optional[List[InParam]] = ...,
) -> Tuple[int, DictIntStringAny]: ...
def o_get_data(
    stored_procedure: String,
    out_params: List[OutParam],
    database: String = ...,
    in_params: Optional[List[InParam]] = ...,
) -> Tuple[BasicDataset, DictIntStringAny]: ...
