from selenium import webdriver

name = input("Enter the name or group name: ")
count = int(input('Number of same msg: '))

chrome = webdriver.Chrome("paste the path of chromedriver")
chrome.get("https://web.whatsapp.com/")
chrome.maximize_window()
input("Press enter after scan: ")

chrome.find_element_by_xpath(f'//span[@title= "{name}"]').click()
msg_box=chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
msg = input("Enter the message: ")

for index in range(count):
    msg_box.send_keys(msg)
    chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()


print("success")