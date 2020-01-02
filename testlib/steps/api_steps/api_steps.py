import allure

from testlib.api.api_calls import ApiCalls


class ApiSteps:
    class Application:
        @allure.step('Get application')
        def get_application(self, app_name=''):
            application = ApiSteps.ApplicationsManagement().get_current_user_applications(name=app_name).json()
            return ApiCalls().Application.get_application(_id=application.get('id'))

        @allure.step('Delete application')
        def delete_application(self, app_name=''):
            application = ApiSteps.ApplicationsManagement().get_current_user_applications(name=app_name).json()
            return ApiCalls().Application.delete_application(_id=application.get('id'))

        @allure.step('Create application')
        def create_application(self, _id=None, custom_id=0, name='', description='', version='', owner_id=None,
                               availability='', connectivity_type=None, connectivity_id=None, connectivity_name=None,
                               timeouts=''):
            return ApiCalls().Application.post_application(custom_id=custom_id, name=name,
                                                           description=description, version=version,
                                                           owner_id=owner_id, availability=availability,
                                                           connectivity_type=connectivity_type,
                                                           connectivity_id=connectivity_id,
                                                           connectivity_name=connectivity_name, timeouts=timeouts)

    class ApplicationsManagement:
        @allure.step('Get current user applications')
        def get_current_user_applications(self, paging_item_count=0, paging_page=0, paging_take=5, sort_column='name',
                                          sort_sort='asc', custom_id='', name='', description='', version='',
                                          availability='', connectivity_method='', timeouts_from='', timeouts_to='',
                                          owner='', deleted=''):
            return ApiCalls().ApplicationManagement.post_applications(paging_item_count=paging_item_count,
                                                                      paging_page=paging_page,
                                                                      paging_take=paging_take,
                                                                      sort_column=sort_column,
                                                                      sort_sort=sort_sort,
                                                                      custom_id=custom_id, name=name,
                                                                      description=description,
                                                                      version=version, availability=availability,
                                                                      connectivity_method=connectivity_method,
                                                                      timeouts_from=timeouts_from,
                                                                      timeouts_to=timeouts_to, owner=owner,
                                                                      deleted=deleted)

    class Auth:
        @allure.step('Log in to IMS system')
        def post_login(self):
            return ApiCalls.Account.post_login(username='username', password='password')

    class UserManagement:
        @allure.step('Create user')
        def create_user(self, password='', confirm_password='', username=''):
            return ApiCalls().UserManagement().post_user(password=password, confirm_password=confirm_password,
                                                         username=username)
