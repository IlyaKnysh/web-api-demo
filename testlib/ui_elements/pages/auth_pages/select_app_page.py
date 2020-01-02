from testlib.helpers import by
from testlib.helpers.extended_element import element
from testlib.ui_elements.base_elements import BasePage
from testlib.ui_elements.blocks.header import Header
from testlib.ui_elements.blocks.navbar import Navbar


class SelectAppPage(BasePage, Header, Navbar):
    connect_icon = element(by.xpath('//div[text()="Connect"]'))

    ss_icon = element(by.xpath('//div[text()="Self-Serve"]'))
