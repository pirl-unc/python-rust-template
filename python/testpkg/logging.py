import logging


def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(
        format='%(asctime)s %(levelname)s [%(funcName)50s()] %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
        force=True
    )
    return logging.getLogger(name)
