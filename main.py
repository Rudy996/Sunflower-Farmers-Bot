import time
from seleniumwire import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_extension("MetaMask.crx")
# options.add_extension("anticaptcha-plugin_v0.58.crx")
options.add_extension("2Captcha Solver.crx")
proxy_options = {
    "proxy": {
        "https": f"http://Login:Password@ip:port"

    }
}
def arbuz():
    try:

        driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe",
                                  options=options, seleniumwire_options=proxy_options)
        private = ("") # Мнемоник
        passw = ("RudyYouTube") # Пароль от метамаска
        cd = 60 # На сколько уходить в сон после посадки
        userbuy = 5 # Сколько купить семян
        hto = 1 # Что покупать?
        Api = ("") # ApiKey RuCaptcha
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")
        print("Начинаем настройку MetaMask")
        time.sleep(1)
        item = driver.find_element_by_xpath("//button[@role='button']")
        print(item)
        print(item.text)
        item.click()
        time.sleep(1)
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/select-action")
        time.sleep(1)
        # item2 = driver.find_element_by_xpath("//button[@class='first-time-flow__button']")
        driver.find_element_by_class_name("first-time-flow__button").click()
        time.sleep(1)
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/metametrics-opt-in")
        time.sleep(1)
        driver.find_element_by_xpath("//button[@data-testid='page-container-footer-next']").click()
        time.sleep(1)
        driver.get(
            "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase")
        time.sleep(1)

        print("Начинаем импортировать ключи и добавлять пароль")
        clu4iki = driver.find_element_by_xpath("//input[@type='password']")
        # clu4iki = driver.find_element_by_xpath("MuiInput-input")
        clu4iki.send_keys(private)
        password1 = driver.find_element_by_id("password")
        password1.send_keys(passw)
        password2 = driver.find_element_by_id("confirm-password")
        password2.send_keys(passw)
        print("Были импортированны ключи и добавлен пароль")
        time.sleep(2)
        driver.find_element_by_class_name("first-time-flow__terms").click()
        time.sleep(2)
        driver.find_element_by_class_name("first-time-flow__button").click()
        time.sleep(5)
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/end-of-flow")
        time.sleep(5)
        driver.find_element_by_class_name("popover-header__button").click()
        time.sleep(2)
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#")
        time.sleep(2)
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network")
        time.sleep(2)
        elems = driver.find_elements_by_class_name("form-field__input")
        print("Начинаем добавлять сеть Polygon")
        time.sleep(2)
        elems[0].send_keys("Matic Mainnet")
        elems[1].send_keys("https://polygon-rpc.com/")
        elems[2].send_keys("137")
        elems[3].send_keys("MATIC")
        elems[4].send_keys("https://explorer.matic.network/")
        print("Сеть Polygon добавлена")
        time.sleep(1)
        driver.find_element_by_class_name("btn-primary").click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("chrome-extension://ifibfemgeogfhoebkmokieepdoobkbpo/options/options.html")
        time.sleep(3)
        driver.find_element_by_xpath("//input[@name='apiKey']").send_keys(Api)
        driver.find_element_by_id("connect").click()
        driver.find_element_by_xpath("//input[@name='autoSolveRecaptchaV2']").click()
        driver.find_element_by_xpath("//input[@name='autoSolveInvisibleRecaptchaV2']").click()
        driver.find_element_by_xpath("//input[@name='autoSolveRecaptchaV3']").click()
        time.sleep(5)
        driver.switch_to.alert.accept()
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://sunflower-land.com/play/")
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[2])
        driver.find_element_by_class_name("btn-primary").click()
        time.sleep(0.5)
        driver.find_element_by_class_name("btn-primary").click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        driver.find_element_by_class_name("bg-brown-200").click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[2])
        driver.find_element_by_class_name("btn-primary").click()
        time.sleep(20)
        driver.switch_to.window(driver.window_handles[1])
        lets_start = driver.find_elements_by_class_name("bg-brown-200")
        lets_start[0].click()
        time.sleep(10)
        while True:
            print("""
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                $$$$$$$$$$$$$$$$$__$$$$$$$$$$$$$$$$$
                $$$$$$$$$$$$$$$$____$$$$$$$$$$$$$$$$
                $$$$___$$$$$$$$$____$$$$$$$$$___$$$$
                $$$$_____$$$$$$$____$$$$$$$_____$$$$
                $$$$___$__$$$$$$____$$$$$$______$$$$
                $$$$___$$__$$$$$____$$$$$__$$___$$$$
                $$$$___$$___$$$$$__$$$$$___$$___$$$$
                $$$$___$$___$$$$$__$$$$$__$$$___$$$$
                $$$$___$$$__$$$$$__$$$$$__$$$___$$$$
                $$$$___$$$__$$$$____$$$$__$$$___$$$$
                $$$$___$$$___$$$____$$$___$$$___$$$$
                $$$$___$$____$$______$$____$$___$$$$
                $$$$______$$$$$__$$__$$$$$______$$$$
                $$$$___$___$$$__$$$$__$$$___$___$$$$
                $$$$___$$_______$$$$_______$$___$$$$
                $$$$___$$$$$__$______$__$$$$$___$$$$
                $$$$___$$$$$__$$$__$$$__$$$$$___$$$$
                $$$$____________________________$$$$
                $$$$$$$$$$$$___$$__$$___$$$$$$$$$$$$
                $$$$$$$$$$$$$___$__$___$$$$$$$$$$$$$
                _$$$$$$$$$$$$$________$$$$$$$$$$$$$_
                _____$$$$$$$$$$$____$$$$$$$$$$$_____
                _________$$$$$$$$$$$$$$$$$$_________   
                """)
            i = 0
            t = 0
            d = 0
            n = 0
            while i != 2:
                try:
                    try:
                        print("Открываю инвентарь")
                        driver.find_element_by_xpath("//img[@alt='inventory']").click()
                        time.sleep(1)
                        print("Выбираю семена")
                        driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/img").click()
                    except:
                        print("")
                    try:
                        print("Закрываю инвентарь")
                        time.sleep(0.5)
                        driver.find_element_by_class_name("h-6").click()
                    except:
                        print("")
                    time.sleep(0.5)
                    # 1 грядка
                    driver.find_element_by_xpath("//div[@id='gameboard']/div[5]/div/div/div/img[2]").click()
                    print(1)
                    driver.find_element_by_xpath("//div[@id='gameboard']/div[5]/div/div/div[2]/img[2]").click()
                    print(2)
                    driver.find_element_by_xpath("//div[@id='gameboard']/div[5]/div/div[2]/div/img[2]").click()
                    print(3)
                    driver.find_element_by_xpath("//div[@id='gameboard']/div[5]/div/div[3]/div/img[2]").click()
                    print(4)
                    driver.find_element_by_xpath("//div[@id='gameboard']/div[5]/div/div[3]/div[2]/img[2]").click()
                    print(5)

                    # Вторая грядка
                    """
                    driver.find_element_by_xpath("//div[@id='cropzone-two']/div/div/img[2]").click()
                    print(6)
                    driver.find_element_by_xpath("//div[@id='cropzone-two']/div[3]/div/img[2]").click()
                    print(7)
                    driver.find_element_by_xpath("//div[@id='cropzone-two']/div[2]/div/img[2]").click()
                    print(8)
                    driver.find_element_by_xpath("//div[@id='cropzone-two']/div/div[2]/img[2]").click()
                    print(9)
                    driver.find_element_by_xpath("//div[@id='cropzone-two']/div[3]/div[2]/img[2]").click()
                    print(10)
                    """


                    # 3 грядка
                    """
                    driver.find_element_by_xpath("//div[@id='cropzone-three']/div/div/img[2]").click()
                    print(11)
                    driver.find_element_by_xpath("//div[@id='cropzone-three']/div[2]/div/img[2]").click()
                    print(12)
                    driver.find_element_by_xpath("//div[@id='cropzone-three']/div/div[2]/img[2]").click()
                    print(13)
                    driver.find_element_by_xpath("//div[@id='cropzone-three']/div[2]/div[2]/img[2]").click()
                    print(14)
                    driver.find_element_by_xpath("//div[@id='cropzone-three']/div/div[3]/img[2]").click()
                    print(15)
                    driver.find_element_by_xpath("//div[@id='cropzone-three']/div[2]/div[3]/img[2]").click()
                    """

                    # 4 грядка
                    """
                    driver.find_element_by_xpath("//div[@id='cropzone-four']/div/div/img[2]").click()
                    print(11)
                    driver.find_element_by_xpath("//div[@id='cropzone-four']/div[2]/div/img[2]").click()
                    print(12)
                    driver.find_element_by_xpath("//div[@id='cropzone-four']/div/div[2]/img[2]").click()
                    print(13)
                    driver.find_element_by_xpath("//div[@id='cropzone-four']/div[2]/div[2]/img[2]").click()
                    print(14)
                    driver.find_element_by_xpath("//div[@id='cropzone-four']/div/div[3]/img[2]").click()
                    print(15)
                    driver.find_element_by_xpath("//div[@id='cropzone-four']/div[2]/div[3]/img[2]").click()
                    """
                except:
                    print("")


                try:
                    print("Выбираю кухню для обхода")
                    kitchen = driver.find_elements_by_class_name("bg-brown-200")
                    try:
                        kitchen[13].click()
                    except:
                        print("")
                    try:
                        kitchen[12].click()
                    except:
                        print("")
                except:
                    print("")


                try:
                    print("Check chest")
                    chest = driver.find_elements_by_class_name("w-16")
                    print("Знайшовся")
                    time.sleep(1)
                    chest[2].click()
                    print("Клац 1")
                    chest[1].click()
                    print("Клац 1")
                except:
                    print("")
                try:
                    print("Закрою сундук, если смогу")
                    cls = driver.find_element_by_class_name("bg-brown-200")
                    print("Ща закрою сундук")
                    time.sleep(2)
                    try:
                        cls[13].click()
                    except:
                        print("")
                    try:
                        cls[13].click()
                    except:
                        print("")
                    print("Сундук закрыли")
                except:
                    print("")
                while t == 0:
                    print("Чек цикла на посадку")
                    time.sleep(cd)
                    t = t + 1
                i = i + 1
            print("Посадил/собрал")
            try:
                try:
                    print("Открываю шоп")
                    driver.find_element_by_xpath("//div[@id='shop']/div/div[2]/span").click()
                    time.sleep(0.5)
                    print("Выбираю продажу")
                    catalog = driver.find_elements_by_class_name("px-1")
                    print("Выбираю категорию с продажей")
                    catalog[1].click()
                    print("Выбрав продажу")
                    time.sleep(1)
                    print("Ищу семена")
                    try:
                        driver.find_element_by_xpath("//div[3]/div/div/div/div/div[2]/div/div/div/img")
                    except:
                        print("")
                    try:
                        seed = driver.find_elements_by_class_name("m-1.5")
                        print("Почти нашел семена")
                        seed[hto].click()
                    except:
                        print("")

                    print("Выбрав семена")
                    time.sleep(1)
                    print("Ищу кнопку для продажи")
                    sell = driver.find_elements_by_class_name("bg-brown-200")
                    print("Нашел кнопки для продажи")
                    sell[15].click()
                    print("Нажал на продажу всех семян")
                    time.sleep(0.5)
                    print("Ищу подтвердить")
                    yes = driver.find_elements_by_class_name("bg-brown-200")
                    print("Почти подтвердил")
                    yes[16].click()
                    print("Подтвердил продажу всего")
                    print("Всё продал")
                except:
                    print("")
                try:
                    time.sleep(0.3)
                    print("Скоро вернусь на покупку")
                    catalog[0].click()
                    print("Вернулся на покупку")
                    time.sleep(1)
                except:
                    print("")
                while n != userbuy:
                    d = d + 1
                    print("Начинаю закупку, но сначало проверю  Sync")
                    try:
                        print("Начинается чек")
                        Sync = driver.find_element_by_class_name("my-1")
                        print("Кто спиздил семена?")
                        bt = driver.find_elements_by_class_name("bg-brown-200")
                        print("Ща нажму на синх")
                        try:
                            bt[13].click()
                        except:
                            print("")
                        try:
                            bt[14].click()
                        except:
                            print("")
                        print("Нажал и жду решение капчи")
                        time.sleep(120)
                        driver.switch_to.window(driver.window_handles[2])
                        time.sleep(5)
                        try:
                            driver.find_element_by_class_name("actionable-message__action--primary").click()
                            time.sleep(5)
                        except:
                            print("")
                        driver.find_element_by_class_name("btn-primary").click()
                        time.sleep(2)
                        driver.switch_to.window(driver.window_handles[1])
                        time.sleep(180)
                        driver.quit()
                        arbuz()
                    except:
                        print("Синхрон не нужен")
                    # seed[hto].click()

                    print("Ща начну покупать")
                    try:
                        driver.find_element_by_xpath("//div[3]/div/div/div/div/div[2]/div/div/div/img").click()
                    except:
                        print("")
                    try:
                        seed = driver.find_elements_by_class_name("m-1.5")
                        print("Почти нашел семена")
                        seed[hto].click()
                    except:
                        print("")


                    buy = driver.find_elements_by_class_name("bg-brown-200")
                    print("Ща как куплю")
                    buy[14].click()
                    print("Купил")
                    n = n + 1
            except:
                print("")

            try:
                driver.find_element_by_class_name("h-6").click()
            except:
                print("")

            print("""
    Создатель - https://www.youtube.com/c/RudyCrypto/featured        
    Пользуешься моим ,отом бесплатно? Тогда ты можешь помочь украинской армии деньгами
    
    НБУ принял решение открыть специальный счет для сбора средств в поддержку Вооруженных Сил Украины.
    Для зачисления средств в национальной валюте:
    Банк: Национальный банк Украины
    МФО 300001
    Счет № UA843000010000000047330992708
    код ЕГРПОУ 00032106
    Получатель: Национальный банк Украины
    
    Благотворительный фонд помощи ветеранам и военным "Повернись живим".
    Для переводов по Украине
    Счет в Ощадбанке:
    IBAN: UA223226690000026007300905964
    ЕГРПОУ: 39696398
    Получатель: Благотворительная Организация "Международный благотворительный фонд "Повернись живим"
    Назначение платежа : Благотворительное пожертвование военнослужащим.
    Счет в ПриватБанке:
    IBAN: UA383052990000026005015017860
    ЕГРПОУ: 39696398
    Получатель: Благотворительная Организация "Международный благотворительный фонд "Вернись живым"
    Назначение платежа: Благотворительное пожертвование военнослужащим.
    Счет Bitcoin Номер: bc1qkd5az2ml7dk5j5h672yhxmhmxe9tuf97j39fm6
    
    Киберполиция создала криптокошельки для сбора средств на потребности борьбы с агрессором
    Собранная криптовалюта пойдет в поддержку Нацполиции, Нацгвардии, Госпогранслужбы и ГСЧС.
    Ethereum -  0x76136B4d578Df727B132053d9a392eeF202F9a80        
    Bitcoin - bc1qdcg86r4rcgf9s6y9nxtyl80xxz62sunw9nevzr
    TRX - TMoeioXTNK1xowtuXFQxnFnf5ZLEJmu7y7
    USDT - TMoeioXTNK1xowtuXFQxnFnf5ZLEJmu7y7
    BNB - 0x76136B4d578Df727B132053d9a392eeF202F9a80
    
    Cyberpolice has created crypto wallet to raise funds to fight the aggressor.
    The collected cryptocurrency will go to supporte National Police, the National Guard, the State Border Guard Service and the State Emergency Service of Ukraine :
    Ethereum - 0x76136B4d578Df727B132053d9a392eeF202F9a80
    Bitcoin - bc1qdcg86r4rcgf9s6y9nxtyl80xxz62sunw9nevzr
    TRX - TMoeioXTNK1xowtuXFQxnFnf5ZLEJmu7y7
    USDT - TMoeioXTNK1xowtuXFQxnFnf5ZLEJmu7y7
    BNB - 0x76136B4d578Df727B132053d9a392eeF202F9a80
                        """)












    except Exception as ex:
        print(ex)
        print("""
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⠛⢿⣿⣿⣿⣿⣿⡿⠀⠀⢀⣿⡄⠀⠀⢻⣿⣿⣿⣿⣿⣿⠟⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠘⣿⣿⣿⣿⣿⠁⠀⠀⣾⣿⣿⡀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⡏⠀⠀⢰⣿⣿⣿⣇⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⣿⠁⠀⠀⣿⣿⣿⣿⣿⡀⠀⠀⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⡿⠀⠀⢠⣿⣿⣿⣿⣿⡇⠀⠀⢹⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣷⠀⠀⢸⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⡇⠀⠀⢻⣿⣿⣿⣿⣿⣿⠀⠀⢀⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⠉⠁⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠈⠉⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⣠⣀⣀⣀⣤⣀⣀⣀⣀⣀⣀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⠻⠛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⢹⣿⠉⠉⣿⣿⠏⠉⠙⣿⣿⡍⠉⠻⠋⠉⣽⡍⠉⢿⡟⠉⣹⠉⠉⣿⠏⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⠉⠀⠀⣿⡟⠀⠰⠀⠘⣿⣿⠆⠀⠀⢾⣿⣿⡄⠈⠀⣴⣿⠀⠀⠃⢀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⠀⠀⡟⠀⢠⣤⣤⠀⠹⠋⠀⣰⡀⠈⢻⡏⠉⢀⣼⣿⣿⠀⠀⣰⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
                """)
    finally:
        driver.close()
        driver.quit()

arbuz()

