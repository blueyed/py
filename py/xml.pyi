from typing import ClassVar, Generic, List, Text, Type, Union
from typing_extensions import Final

class _NamespaceMetaclass(type):
    def __getattr__(self, name: str) -> Type[Tag]: ...

class Namespace(metaclass=_NamespaceMetaclass): ...

# TODO: An element of Tag can be a list itself, but this crashes
# mypy currently (mypy 0.770): https://github.com/python/mypy/issues/6730
# At least it works in __init__() so most of the time it won't be noticed.
class Tag(List[Union[Text, Tag, raw]]):
    class Attr:
        def __getattr__(self, attr: str) -> Text: ...
    attr: Final[Attr]
    def __init__(self, *args: Union[Text, Tag, raw, List[Union[Text, Tag, raw]]], **kwargs: Union[Text, raw]) -> None: ...
    def unicode(self, indent: int = ...) -> Text: ...

class html(Namespace):
    class Style:
        def __init__(self, **kw: Union[str, Text]) -> None: ...
    style: ClassVar[Style]

class raw:
    uniobj: Final[Text]
    def __init__(self, uniobj: Text) -> None: ...

def escape(ustring: Union[str, Text]) -> Text: ...
