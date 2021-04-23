from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import json


def streaming(url):
    options = webdriver.ChromeOptions() 
    options.add_argument(r"user-data-dir=C:\Users\Will\AppData\Local\Google\Chrome\User Data\Default")

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    acc_index = 0
    links = []
    titles = []
    dates = []
    i = 2

    while (acc_index < 11):

        if not i == 22:
            element = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div/div[4]/div[5]/table/tbody/tr[1]/td/table/tbody/tr['+str(i)+']/td[2]/div/div/span[2]/span/a')
            lnk = element.get_attribute('href')
            driver.get(lnk)
        else:
            break



        try:
            now = datetime.now()
            try:
                elem1 = driver.find_element_by_xpath("//a[contains(@href, 'throwbin')]")
            except:
                try:
                    elem1 = driver.find_element_by_xpath("//a[contains(@href, 'mega.nz')]")
                except:
                    elem1 = driver.find_element_by_xpath("//a[contains(@href, 'ghostbin.co')]")
            elem2 = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div/div[3]/div[1]/h1')
            link = elem1.get_attribute('href')
            title = elem2.get_attribute('text')

            links.append(elem1.get_attribute('href'))
            titles.append(elem2.text)
            dates.append(now.strftime("%d/%m/%Y %H:%M:%S"))
            acc_index += 1
            i += 1
            driver.get(url)
            print('Got account')
            driver.get(url)
        except:
            i += 1
            driver.get(url)


    print(list(zip(titles, dates, links)))

    with open('accounts/streaming.json') as f:
        accounts_list = json.load(f)
        accounts_list['account'] = []

    for title, date, link in zip(titles, dates, links):
        
        with open('accounts/streaming.json') as json_file:
            accounts_list['account'].append({
                'title':title,
                'date':date,
                'link':link
            })
    
        with open('accounts/streaming.json', 'w') as f:
            json.dump(accounts_list, f)


if __name__ == '__main__':
    streaming('https://cracked.to/Forum-Streaming--108?sortby=started&order=desc&datecut=9999&prefix=0')