import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestEmployeeKZ:

    browser_employee: WebDriver

    def setup(self):
        self.phone = '8888881114'
        self.sms = '5555'
        self.password = '1!QWERTy'
        self.last_name = 'Исконный'
        self.first_name = 'Фонарь'
        self.middle_name = 'Демокритович'
        self.series = '2630'
        self.number = '835642'
        self.number_kz = '83564222'
        self.pasport_data = '20092022'
        self.code = '884554'
        self.who_give = 'МП № 88 ОУФМС РОССИИ ПО САНКТ-ПЕТЕРБУРГУ И ЛЕНИНГРАДСКОЙ ОБЛ. В ВОЛОСОВСКОМ РАЙОНЕ'
        self.place_of_birth = 'Москва'
        self.inn = '259077600050'
        self.registration_address = 'телеви'
        self.country = 'Казахстан'

    def open_employee(self):
        self.browser_employee = webdriver.Chrome()
        self.browser_employee.get('https://dev.mobistaff.ru/employee/login')
        self.browser_employee.maximize_window()

    def close_employee(self):
        self.browser_employee.quit()

    def registration_employee_kz(self):
        time.sleep(1)
        self.browser_employee.find_element(By.ID, 'phone').send_keys(self.phone)
        self.browser_employee.find_element(By.ID, 'agree').click()
        self.browser_employee.find_element(By.XPATH, "//button[contains(text(),'Далее')]").click()
        WebDriverWait(self.browser_employee, 30).until(
            EC.visibility_of_element_located((By.ID, 'code'))).send_keys(self.sms)
        self.browser_employee.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(self.browser_employee, 30).until(
            EC.visibility_of_element_located((By.ID, 'password'))).send_keys(self.password)
        self.browser_employee.find_element(By.ID, 'password_confirm').send_keys(self.password)
        self.browser_employee.find_element(By.XPATH, "//button[contains(text(),'Сохранить')]").click()
        WebDriverWait(self.browser_employee, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Далее')]"))).click()
        time.sleep(1)
        self.browser_employee.find_element(By.CSS_SELECTOR, 'input.form-input').send_keys("17091978")
        self.browser_employee.find_element(By.XPATH, "//label[contains(text(),'Отчество')]").click()
        self.browser_employee.find_element(By.ID, 'last_name').send_keys(self.last_name)
        self.browser_employee.find_element(By.ID, 'first_name').send_keys(self.first_name)
        self.browser_employee.find_element(By.ID, 'middle_name').send_keys(self.middle_name)
        self.browser_employee.find_element(By.ID, 'gender-male').click()
        self.browser_employee.find_element(By.CSS_SELECTOR, "input.vue-treeselect__input").send_keys(self.country)
        time.sleep(0.5)
        self.browser_employee.find_element(By.CSS_SELECTOR, "input.vue-treeselect__input").send_keys(Keys.ENTER)
        self.browser_employee.find_element(By.XPATH, "//button[contains(text(),'Далее')]").click()
        time.sleep(2)
        self.browser_employee.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div[2]/div/button/input").send_keys(
            "C:\\q.jpg")
        self.browser_employee.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div/button/input").send_keys(
            "C:\\q.jpg")
        self.browser_employee.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div/div/div[1]/div[3]/div[2]/div/button/input").send_keys(
            "C:\\q.jpg")
        self.browser_employee.find_element(By.ID, 'series').send_keys(self.series)
        self.browser_employee.find_element(By.ID, 'number').send_keys(self.number)
        self.browser_employee.find_element(
            By.XPATH,
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[3]/div[1]/span[1]/input[1]"
        ).send_keys(self.pasport_data)
        self.browser_employee.find_element(By.ID, 'place-of-birth').send_keys(self.place_of_birth)
        self.browser_employee.find_element(By.XPATH, "//button[contains(text(),'Далее')]").click()
        time.sleep(2)
        self.browser_employee.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div[2]/div/button/input").send_keys(
            "C:\\q.jpg")
        self.browser_employee.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div/button/input").send_keys(
            "C:\\q.jpg")
        self.browser_employee.find_element(By.CSS_SELECTOR, "input.form-input").send_keys(self.pasport_data)
        self.browser_employee.find_element(By.XPATH, "//button[contains(text(),'Далее')]").click()
        time.sleep(2)
        self.browser_employee.find_element(
            By.CSS_SELECTOR,
            'input.uppy-DragDrop-input').send_keys(
            "C:\\q.jpg")
        self.browser_employee.find_element(By.CSS_SELECTOR, "input.vue-treeselect__input").send_keys('Работа')
        time.sleep(0.5)
        self.browser_employee.find_element(By.CSS_SELECTOR, "input.vue-treeselect__input").send_keys(Keys.ENTER)
        self.browser_employee.find_element(By.ID, 'series').send_keys(self.series)
        self.browser_employee.find_element(By.ID, 'number').send_keys(self.number)
        self.browser_employee.find_element(By.CSS_SELECTOR, "input.form-input").send_keys(self.pasport_data)
        self.browser_employee.find_element(By.XPATH, "//button[contains(text(),'Далее')]").click()

        self.browser_employee.get('https://dev.mobistaff.ru/employee/profile')
        time.sleep(1)
        self.browser_employee.find_element(By.ID, "registration_address").send_keys(self.registration_address)
        WebDriverWait(self.browser_employee, 30).until(EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'г Новосибирск, ул Телевизионная')]"))).click()
        self.browser_employee.find_element(By.ID, "inn").send_keys(self.inn)
        time.sleep(1)
        self.browser_employee.find_element(By.XPATH, "//button[contains(text(),'Сохранить')]").click()

    def login_employee_kz(self):
        time.sleep(1)
        self.browser_employee.find_element(By.ID, 'phone').click()
        self.browser_employee.find_element(By.ID, 'phone').send_keys(self.phone)
        self.browser_employee.find_element(By.ID, 'agree').click()
        self.browser_employee.find_element(By.XPATH, "//button[contains(text(),'Далее')]").click()
        WebDriverWait(self.browser_employee, 30).until(
            EC.presence_of_element_located((By.ID, 'password')))
        self.browser_employee.find_element(By.ID, 'password').send_keys(self.password)
        self.browser_employee.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        WebDriverWait(self.browser_employee, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Позже')]"))).click()
        assert WebDriverWait(self.browser_employee, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Заявки')]")))

    def employee_del_kz(self):
        self.browser_employee.find_element(By.XPATH,
                                           "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
        self.browser_employee.find_element(By.XPATH, "//a[contains(text(),'Настройки')]").click()
        WebDriverWait(self.browser_employee, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Удалить профиль безвозвратно')]"))).click()
        WebDriverWait(self.browser_employee, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".swal2-confirm"))).click()
        assert WebDriverWait(self.browser_employee, 30).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Ваш аккаунт был успешно удален')]")))

    def test_registration_employee_kz(self):
        self.open_employee()
        self.registration_employee_kz()
        assert WebDriverWait(self.browser_employee, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Заявки')]")))
        time.sleep(5)
        self.close_employee()

    def test_login_employee_kz(self):
        self.open_employee()
        self.login_employee_kz()
        time.sleep(5)
        self.close_employee()

    def test_employee_del_kz(self):
        self.open_employee()
        self.login_employee_kz()
        time.sleep(1)
        self.employee_del_kz()
        time.sleep(5)
        self.close_employee()