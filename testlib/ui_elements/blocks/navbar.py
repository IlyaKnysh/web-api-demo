from testlib.helpers import by
from testlib.helpers.extended_element import element
from testlib.ui_elements.base_elements import BasePage, BaseEnum


class Navbar(BasePage):
    dashboard_button = element(by.xpath('//a[child::span[text()="Dashboard"]]'))

    platform_management_button = element(by.xpath('//a[child::span[text()="Platform Management"]]'))

    virtual_workforce_button = element(by.xpath('//a[child::span[text()="Virtual Workforce"]]'))

    design_studio_button = element(by.xpath('//a[child::span[text()="Design Studio"]]'))

    automation_lifecycle_button = element(by.xpath('//a[child::span[text()="Automation Lifecycle"]]'))

    queue_management_button = element(by.xpath('//a[child::span[text()="Queue Management"]]'))

    self_serve_button = element(by.xpath('//a[child::span[text()="Self-Serve"]]'))

    cognitive_services_button = element(by.xpath('//a[child::span[text()="Cognitive Services"]]'))

    platform_builder_button = element(by.xpath('//a[child::span[text()="Platform Builder"]]'))

    class PlatformManagement(BaseEnum):
        VIRTUAL_WORKER_SETTINGS = 'Virtual Worker Settings'
        LICENSE_MANAGER = 'License Manager'

        @property
        def get_option(self):
            Navbar.platform_management_button.click()
            return self._get()

    class VirtualWorkforce(BaseEnum):
        UTILIZATION = 'Utilization'
        LIVE_SESSIONS = 'Live Sessions'
        PERFORMANCE = 'Performance'
        LIVE_ACCESS = 'Live Access'

        @property
        def get_option(self):
            Navbar.virtual_workforce_button.click()
            return self._get()

    class DesignStudio(BaseEnum):
        WIREFRAMER = 'Wireframer'
        PROCESS_OBJECT_EXPLORER = 'Process/Object Explorer'
        ENVIRONMENT_DATA_ITEMS = 'Environment Data Items'
        ENVIRONMENT_LOCKS = 'Environment Locks'

        @property
        def get_option(self):
            Navbar.design_studio_button.click()
            return self._get()

    class AutomationLifecycle(BaseEnum):
        BUSINESS_PROCESSES = 'Business Processes'
        APPLICATIONS = 'Applications'
        PROCESS_DEFINITIONS = 'Process Definitions'
        EXCEPTIONS = 'Exceptions'

        @property
        def get_option(self):
            Navbar.automation_lifecycle_button.click()
            return self._get()

    class QueueManagement(BaseEnum):
        QUEUES_OVERVIEW = 'Queues Overview'
        QUEUES_MANAGER = 'Queues Manager'
        QUEUES_ANALYZER = 'Queues Analyzer'

        @property
        def get_option(self):
            Navbar.queue_management_button.click()
            return self._get()

    class SelfServe(BaseEnum):
        FORMS = 'Forms'

        @property
        def get_option(self):
            Navbar.self_serve_button.click()
            return self._get()

    class CognitiveServices(BaseEnum):
        NLU = 'NLU'

        @property
        def get_option(self):
            Navbar.cognitive_services_button.click()
            return self._get()

    class PlatformBuilder(BaseEnum):
        PLATFORM_BUILDER = 'Platform Builder'

        @property
        def get_option(self):
            Navbar.platform_builder_button.click()
            return element(by.xpath(f'//li/a[@href]/span[contains(text(), "{self.value}")]'))
