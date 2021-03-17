from selenium import webdriver

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
WEBSITE = "https://www.python.org/"
# driver.get("https://www.amazon.com/Philips-HD9641-96-Turbostar-Airfryer/dp/B07VH2CXPJ/ref=sxin_10?ascsubtag=amzn1.osa.45996ac2-3fd3-461d-b753-908c65fe0aec.ATVPDKIKX0DER.en_US&creativeASIN=B06Y39KPZ4&cv_ct_cx=air%2Bfryer&cv_ct_id=amzn1.osa.45996ac2-3fd3-461d-b753-908c65fe0aec.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-earns-comm&dchild=1&keywords=air%2Bfryer&linkCode=oas&pd_rd_i=B06Y39KPZ4&pd_rd_r=d758c7d8-97bb-4a06-9e62-edd7fca12044&pd_rd_w=K2er7&pd_rd_wg=GVurr&pf_rd_p=35b32c02-1b41-4e49-9b89-0297af2446e1&pf_rd_r=9PCDM5HSB588G043PJMJ&qid=1615368382&s=kitchen&sr=1-1-64f3a41a-73ca-403a-923c-8152c45485fe&tag=real-homes-20&th=1")
# price=driver.find_elements_by_id("priceblock_ourprice")
# print(price[0].text)
event_list = {}
# driver.close()  # close the active tab
# driver.quit()  # quit the entire program
driver.get(WEBSITE)

event_date = driver.find_elements_by_css_selector(".event-widget time")
event_name = driver.find_elements_by_css_selector(".event-widget li a")
for n in range (len(event_date)):
    event_list[n] ={
        "time": event_date[n].text,
        "name": event_name[n].text,
    }
print(event_list)
driver.close()  # close the active tab
driver.quit()  # quit the entire program
