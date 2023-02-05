from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
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

generateReport('Total Tag Unique -> ' + str(len(cleanData)))

for i in cleanData:

    if i == "" :
        totalTagWitouthLink+=1
    else :
        # script = driver.execute_script("window.open('"+link+"','_blank');")
        st = time.time()
        response = requests.get(i)
        et = time.time() - st
        # get the status code from the response object
        status_code = str(response.status_code)

        report_generate = ""
        print("Current Link " + i)
        if status_code == "200":
            report_generate = i + " Status Code : " + status_code + " -> Success " + str(et) + "/s"
        else:
            report_generate = i + " Status Code : " + status_code + " -> Error " + str(et) + "/s"
            print("Current Link " + i + ", Status Code " + status_code)

        generateReport(report_generate)
        totalTagWithLink+=1

generateReport('Total WithLink(uniq) -> ' + str(totalTagWithLink))
generateReport('Total WithOutLink -> ' + str(totalTagWitouthLink))
