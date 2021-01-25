from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import geckodriver_autoinstaller
import sys
import random
from random import randint
import time
import schedule


geckodriver_autoinstaller.install()

driver = webdriver.Firefox()

action_chains = ActionChains(driver)
action_chains.send_keys(Keys.ARROW_DOWN)

link = ["https://techforhack.com/84-woocommerce-extensions-updates/",
            "https://techforhack.com/56-woocommerce-extensions-updates/",
            "https://techforhack.com/newspaper-v10-3-7-wordpress-news-theme/",
            "https://techforhack.com/elementor_pro_3-0-4_nulled/",
            "https://techforhack.com/adobe-cc-2020-universal-crack-for-adobe-cc-2020-full-version/",
            "https://techforhack.com/wireshark-termux/",
            "https://techforhack.com/windows-10-kali-linux-subsystem-full-tutorial/",
            "https://techforhack.com/tool-x/",
            "https://techforhack.com/routersploit/",
            "https://techforhack.com/newspaper-v10-3-7-wordpress-news-theme/",
            "https://techforhack.com/networkingfundamentals/",
            "https://techforhack.com/networkdevices/",
            "https://techforhack.com/portable_hacking_device/",
            "https://techforhack.com/tbomber/",
            "https://techforhack.com/metasploit-termux/",
            "https://techforhack.com/lazy_script/",
            "https://techforhack.com/nethunter-on-android/",
            "https://techforhack.com/install-hidden-eye-advanced-phishing-tool-full-guide/",
            "https://techforhack.com/instagram-tools-hack-insta-from-termux/",
            "https://techforhack.com/black_hydra/",
            "https://techforhack.com/nmap/",
            "https://techforhack.com/hackpro/",
            "https://techforhack.com/fix-any-android-game-lag-in-few-minutes/",
            "https://techforhack.com/elementor_pro_3-0-4_nulled/",
            "https://techforhack.com/ddos-termux/",
            "https://techforhack.com/databasetechnology/",
            "https://techforhack.com/database-models-all-you-need-to-know/",
            "https://techforhack.com/metasploit-payload-termux/"
            ]


def scroll_down():
    i = 0
    print("scrolling down")
    while i < 150:
        action_chains.perform()
        time.sleep(0.1)
        i = i+1


def scroll_up():
    i = 0
    print("scrolling up")
    while i < 150:
        action_chains.perform()
        i = i+1


def ran_time():
    sec = randint(20, 45)
    print("wait", sec, "seconds")
    for remaining in range(sec, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rComplete!            \n")


def small_ran_time():
    sec = randint(7, 12)
    print("wait", sec, "seconds")
    for remaining in range(sec, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rComplete!            \n")


def loop():
    global completed_views
    print("Evil_Shade - Traffic Bot")
    print("##################################################################################")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#                             Generate free traffic                              #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("##################################################################################")

    i = randint(300, 1000)
    print(i, "Views Generated")
    try:
        completed_views = 0
        while i > 0:
            ran_link = random.choice(link)
            driver.get(ran_link)
            print("opening link", ran_link)
            small_ran_time()
            scroll_down()
            scroll_up()
            ran_time()

            i -= 1
            completed_views += 1
            print("--------------------------------------------------:")

    except Exception as e:
        print(e)
        print("you got", completed_views, "visitors")

    print("you got", completed_views, "visitors")


if __name__ == '__main__':
    loop()
    # schedule.every(5).seconds.do(loop)
    # schedule.every().hour.do(job)
    schedule.every().day.at("24:00").do(loop)
    # schedule.every(5).to(10).minutes.do(job)
    # schedule.every().monday.do(job)
    # schedule.every().wednesday.at("13:15").do(job)
    # schedule.every().minute.at(":17").do(job)

    while True:
        print('Waiting for right time')
        schedule.run_pending()
        time.sleep(1)
