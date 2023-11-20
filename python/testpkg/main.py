from .logging import get_logger
from testpkg import testpkgrs


logger = get_logger(__name__)


def add_numbers(value_1: int, value_2: int):
    summed_value = testpkgrs.add_numbers(value_1, value_2)
    logger.info(summed_value)