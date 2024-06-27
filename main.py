import time

from core import constants, utils
from core.driver import driver


def main(driver):
    utils.connect_wallet_with_metamask(driver=driver)
    time.sleep(constants.TIME_DELAY)


main(driver=driver)
