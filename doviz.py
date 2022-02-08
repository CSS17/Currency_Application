from selenium import webdriver
ayarlar=webdriver.ChromeOptions()
ayarlar.headless=True
driver=webdriver.Chrome(options=ayarlar)


def dolar():
    driver.get("https://www.bloomberght.com/doviz/dolar")  
    try :
        return driver.find_element_by_class_name("LastPrice.upGreen").text
    except:
        return driver.find_element_by_class_name("LastPrice.downRed").text

def euro():
    driver.get("https://www.bloomberght.com/doviz/euro")  
    try :
        return driver.find_element_by_class_name("LastPrice.upGreen").text
    except:
        return driver.find_element_by_class_name("LastPrice.downRed").text


def sterlin():
    driver.get("https://www.bloomberght.com/doviz/ingiliz-sterlini")  
    try :
        return driver.find_element_by_class_name("LastPrice.upGreen").text
    except:
        return driver.find_element_by_class_name("LastPrice.downRed").text
    
def altın():
    driver.get("https://www.bloomberght.com/altin/gram-altin")  
    try :
        return driver.find_element_by_class_name("LastPrice.upGreen").text
    except:
        return driver.find_element_by_class_name("LastPrice.downRed").text 

def btc():
    driver.get("https://www.bloomberght.com/doviz/bitcoin")  
    try :
        return driver.find_element_by_class_name("LastPrice.upGreen").text
    except:
        return driver.find_element_by_class_name("LastPrice.downRed").text

   



