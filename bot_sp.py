from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

warnings.simplefilter("ignore")

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://cdn.botpress.cloud/webchat/v1/index.html?options=%7B%22config%22%3A%7B%22composerPlaceholder%22%3A%22Talk%20to%20Jarvis%22%2C%22botConversationDescription%22%3A%22Virtual%20Assistant%22%2C%22botId%22%3A%22cca71124-a7c4-4fd5-97d4-297b24f433e1%22%2C%22hostUrl%22%3A%22https%3A%2F%2Fcdn.botpress.cloud%2Fwebchat%2Fv1%22%2C%22messagingUrl%22%3A%22https%3A%2F%2Fmessaging.botpress.cloud%22%2C%22clientId%22%3A%22cca71124-a7c4-4fd5-97d4-297b24f433e1%22%2C%22webhookId%22%3A%22df2d4573-d77a-466f-89b6-9bc19bc470ad%22%2C%22lazySocket%22%3Atrue%2C%22themeName%22%3A%22prism%22%2C%22botName%22%3A%22JarvisAI%22%2C%22stylesheet%22%3A%22https%3A%2F%2Fwebchat-styler-css.botpress.app%2Fprod%2Ff292e765-a62e-46de-8f68-731825670bae%2Fv81880%2Fstyle.css%22%2C%22frontendVersion%22%3A%22v1%22%2C%22useSessionStorage%22%3Atrue%2C%22showBotInfoPage%22%3Atrue%2C%22enableConversationDeletion%22%3Atrue%2C%22theme%22%3A%22prism%22%2C%22themeColor%22%3A%22%232563eb%22%2C%22chatId%22%3A%22bp-web-widget%22%2C%22encryptionKey%22%3A%22QkjM6TiK97twBBz8YxFK45fK102zfusc%22%7D%7D')
sleep(3)


def click_on_chat_button():
    button = driver.find_element(By.XPATH, '/html/body/div/div/button').click()
    sleep(2)
    while True:
        try:
            loader = driver.find_element(
                By.CLASS_NAME, 'bpw-msg-list-loading')
            is_visible = loader.is_displayed()
            print('Initializing Jarvis...')

            if not is_visible:
                break
            else:
                pass
        except NoSuchElementException:
            print('Jarvis is Initializing.')
            break
        sleep(1)


def click_on_conversation():
    button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/button').click()
    sleep(2)


def start_conversation():
    
    driver.find_element(by=By.XPATH,value="/html/body/div/div/div/div[2]/div[2]/div[2]/div/textarea").send_keys("Hello")
    sleep(1)
    driver.find_element(by=By.XPATH,value="/html/body/div/div/div/div[2]/div[2]/div[2]/div/div/button").click() 


def ChatGPTBrain(Query):
    Query = str(Query)
    driver.find_element(by=By.XPATH,value="/html/body/div/div/div/div[2]/div[2]/div[2]/div/textarea").send_keys(Query)
    sleep(1)
    driver.find_element(by=By.XPATH,value="/html/body/div/div/div/div[2]/div[2]/div[2]/div/div/button").click()
    sleep(1)


def isBubbleLoaderVisible():
    print('jarvis Is Typing...')
    while True:
        try:
            bubble_loader = driver.find_element(
                By.CLASS_NAME, 'bpw-typing-group')
            is_visible = bubble_loader.is_displayed()

            if not is_visible:
                break
            else:
                pass
        except NoSuchElementException:
            print('Jarvis Is Sending Mesage...')
            break
        sleep(1)


chatnumber = 2


def retriveData():
    print('Retriving Chat...')
    global chatnumber
    sleep(1)
    try:
        p = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
        By.XPATH, f'/html/body/div/div/div/div[2]/div[1]/div/div/div[{chatnumber}]/div/div[2]/div/div/div/div/div/p')))
        print("\nJarvis: " + p.text)
        chatnumber = chatnumber + 2
        return(p.text)
    except:
        print("Element not found within 10 seconds")

# click_on_chat_button()
# click_on_conversation()
# start_conversation()

# while True:
#     Query = input('You: ')
    
#     ChatGPTBrain(Query=Query)
#     isBubbleLoaderVisible()
#     retriveData()
    


# /html/body/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div/p
#/html/body/div/div/div/div[2]/div[1]/div/div/div[4]/div/div[2]/div/div/div/div/div/p
#/html/body/div/div/div/div[2]/div[1]/div/div/div[6]/div/div[2]/div/div/div/div/div/p
#copyfullxpath
