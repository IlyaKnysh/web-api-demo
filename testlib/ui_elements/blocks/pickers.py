from testlib.helpers import by
from testlib.helpers.extended_element import element


class Calendar:
    @staticmethod
    def get_date(date):
        return element(by.xpath(f'//div[@class="rc-calendar-date" and text()="{date}"]'))

    ok_button = element(by.xpath('//a[contains(@class, "rc-calendar-ok-btn")]'))


class TimeSelector:
    hours_field = element(by.xpath('//input[@aria-label="Hour"]'))

    minute_field = element(by.xpath('//input[@aria-label="Minute"]'))

    second_field = element(by.xpath('//input[contains(@class,"flatpickr-second")]'))

    part_button = element(by.xpath('//span[@class="flatpickr-am-pm"]'))
