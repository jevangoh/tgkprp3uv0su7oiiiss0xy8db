from importlib.metadata import version, PackageNotFoundError
from .tgkprp3uv0su7oiiiss0xy8db import tgkprp3uv0su7oiiiss0xy8db as _

try:
    __version__ = version("tgkprp3uv0su7oiiiss0xy8db")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["_", "__version__"]
