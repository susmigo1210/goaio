import platform
from goaio.utils.loghandler import get_logger

prop_logger = get_logger(file_name=__name__)


def is_mac() -> bool:
    return "Darwin" in platform.uname()


def is_windows() -> bool:
    return "Windows" in platform.uname()


def is_linux() -> bool:
    return "Linux" in platform.uname()


if __name__ == "__main__":
    print(is_mac())
