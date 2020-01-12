from typing import Callable, Iterator, Mapping, Optional, Tuple, TypeVar, Union
from typing_extensions import Final

_D = TypeVar('_D')
_T = TypeVar('_T')

class ParseError(Exception):
    path: Final[str]
    lineno: Final[int]
    msg: Final[str]
    def __init__(self, path: str, lineno: int, msg: str) -> None: ...

class _SectionWrapper:
    config: Final[IniConfig]
    name: Final[str]
    def __init__(self, config: IniConfig, name: str) -> None: ...
    def __getitem__(self, key: str) -> str: ...
    def __iter__(self) -> Iterator[str]: ...
    def get(self, key: str, default: _D = ..., convert: Callable[[Optional[str]], _T] = ...) -> Union[_T, _D]: ...
    def items(self) -> Iterator[Tuple[str, Optional[str]]]: ...
    def lineof(self, name: str) -> Optional[int]: ...

class IniConfig:
    path: Final[str]
    sections: Final[Mapping[str, Mapping[str, Optional[str]]]]
    def __init__(self, path: str, data: Optional[str] = None): ...
    def __contains__(self, arg: str) -> bool: ...
    def __getitem__(self, name: str) -> _SectionWrapper: ...
    def __iter__(self) -> Iterator[_SectionWrapper]: ...
    def get(self, section: str, name: str, default: _D = ..., convert: Callable[[Optional[str]], _T] = ...) -> Union[_T, _D]: ...
    def lineof(self, section: str, name: Optional[str] = ...) -> Optional[int]: ...
