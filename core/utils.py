import time
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from core import constants


def log(message, level="INFO"):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{current_time} - {level} - {message}")


def close_other_tab(driver):
    current_window = driver.current_window_handle
    all_windows = driver.window_handles

    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            driver.close()
    driver.switch_to.window(current_window)


def connect_wallet_with_metamask(driver):
    log("Bắt đầu :: kết nối ví metamask", "INFO")
    log("Đang chạy :: cài đặt ví metamask ...", "INFO")
    driver.get(constants.METAMASK_EXTENSION_URL)
    time.sleep(constants.TIME_DELAY_ADD_EXTENSION)
    log("Đang chạy :: cài đặt ví metamask thành công", "INFO")

    close_other_tab(driver=driver)

    exactly_agree_btn = WebDriverWait(driver, constants.TIME_OUT).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, constants.EXACTLY_AGREE_BTN_SELECTOR))
    )
    exactly_agree_btn.click()

    log("Đang chạy :: nhập ví vào metamask ...", "INFO")
    import_wallet_btn = WebDriverWait(driver, constants.TIME_OUT).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, constants.IMPORT_WALLET_BTN_SELECTOR))
    )
    import_wallet_btn.click()

    agree_btn = WebDriverWait(driver, constants.TIME_OUT).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, constants.AGREE_BTN_SELECTOR))
    )
    agree_btn.click()

    for index in range(0, 12):
        secret_input = WebDriverWait(driver, constants.TIME_OUT).until(
            ec.presence_of_element_located((By.ID, f'import-srp__srp-word-{index}'))
        )
        secrets = constants.SECRETS.split(' ')
        secret_input.send_keys(secrets[index])

    confirm_secret_btn = WebDriverWait(driver, constants.TIME_OUT).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, constants.CONFIRM_SECRET_BTN_SELECTOR))
    )
    confirm_secret_btn.click()

    new_password_input = WebDriverWait(driver, constants.TIME_OUT).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, constants.NEW_PASSWORD_INPUT_SELECTOR))
    )
    new_password_input.send_keys(constants.PASSWORD_WALLET)

    confirm_new_password_input = WebDriverWait(driver, constants.TIME_OUT).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, constants.CONFIRM_NEW_PASSWORD_INPUT_SELECTOR))
    )
    confirm_new_password_input.send_keys(constants.PASSWORD_WALLET)

    checkbox_new_password_btn = WebDriverWait(driver, constants.TIME_OUT).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, constants.CHECKBOX_NEW_PASSWORD_SELECTOR))
    )
    checkbox_new_password_btn.click()

    confirm_import_wallet_btn = WebDriverWait(driver, constants.TIME_OUT).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, constants.CONFIRM_IMPORT_WALLET_BTN_SELECTOR))
    )
    confirm_import_wallet_btn.click()

    got_it_btn = WebDriverWait(driver, constants.TIME_OUT).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, constants.GOT_IT_BTN_SELECTOR))
    )
    got_it_btn.click()

    next_btn = WebDriverWait(driver, constants.TIME_OUT).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, constants.NEXT_DONE_METAMASK_BTN_SELECTOR))
    )
    next_btn.click()

    done_btn = WebDriverWait(driver, constants.TIME_OUT).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, constants.NEXT_DONE_METAMASK_BTN_SELECTOR))
    )
    done_btn.click()

    enable_btn = WebDriverWait(driver, constants.TIME_OUT).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, constants.ENABLE_METAMASK_BTN_SELECTOR))
    )
    enable_btn.click()

    log("Đang chạy :: nhập ví vào metamask thành công", "INFO")
    log("Kết thúc :: kết nối ví metamask thành công", "INFO")
