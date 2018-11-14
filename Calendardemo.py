from selenium import webdriver


class CalendarDemo:
    def test(self):
        base_url = "https://consumer.hottab.us/"
        driver = webdriver.Chrome()
        driver.get(base_url)


calendar = CalendarDemo()
calendar.test()

# comment test commit
