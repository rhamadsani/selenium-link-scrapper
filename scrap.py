from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def generateReport(message):
    with open("test-report.txt", "a") as f:
        f.write(message)
        f.write("\n")


driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.jetorbit.com')

aHref = driver.find_elements(By.TAG_NAME, 'a')
generateReport('Total Tag -> ' + str(len(aHref)))
totalTagWithLink = 0
totalTagWitouthLink = 0


def unique(list1):
    unique_list = []

    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    
    return unique_list

def cleanList(list2):
    data_list = []
    for x in list2:
        data_list.append(x.get_attribute("href"))

    return data_list

cleanData = cleanList(aHref)
cleanData = unique(cleanData)

for i in cleanData:
    # script = driver.execute_script("window.open('"+link+"','_blank');")
    script = driver.execute_script("window.location.href='"+i+"'")
    time.sleep(4)
    current_link = driver.current_url
    report_generate = ""
    if current_link == i: 
        report_generate = i + " -> Success"
    else : 
        report_generate = i + " -> Error"
        print(current_link, i)
    
    generateReport(report_generate)
    if i == "" :
        totalTagWitouthLink+=1
    else :
        totalTagWithLink+=1

generateReport('Total WithLink(uniq) -> ' + str(totalTagWithLink))
generateReport('Total WithOutLink -> ' + str(totalTagWitouthLink))
