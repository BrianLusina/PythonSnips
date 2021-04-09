import logging
import random

logger = logging.getLogger()


def say_num():
    num = random.choice(range(0, 50))
    logger.debug(num)
    return num


# necessary for logging to work
if __name__ == "__main__":
    logging.basicConfig(filename="example.log", level=logging.DEBUG)
    say_num()
