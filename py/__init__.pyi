# py allows to use e.g. py.path.local even without importing py.path.
# So import implicitly.
from . import error
from . import iniconfig
from . import path
from . import io
from . import xml

__version__: str
