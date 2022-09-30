from typing import Any

from com.inductiveautomation.ignition.common.model.values import BasicQualifiedValue
from incendium.helper.types import String

def read(tag_path: String) -> BasicQualifiedValue: ...
def write(tag_path: String, value: Any) -> int: ...
