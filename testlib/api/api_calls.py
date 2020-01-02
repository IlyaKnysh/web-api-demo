from config.env import ENV
from testlib.api.helpers_api import BaseApi


class ApiCalls(BaseApi):
    api_url = ENV

    def __init__(self, required_token=True):
        if required_token:
            self.get_headers['Authorization'] = f'Bearer {BaseApi.token}'
            self.post_headers['Authorization'] = f'Bearer {BaseApi.token}'

    class Application:
        @staticmethod
        def get_application(_id=None):
            return ApiCalls.api_get(f'/api/project-management/application/{_id}')

        @staticmethod
        def delete_application(_id=None):
            return ApiCalls.api_delete(f'/api/project-management/application/{_id}')

        @staticmethod
        def put_application(_id=None, custom_id=None, name=None, description=None, version=None, owner_id=None,
                            availability=None, connectivity_type=None, connectivity_id=None, connectivity_name=None,
                            timeouts=None):
            params = {
                "id": _id,
                "customId": custom_id,
                "name": name,
                "description": description,
                "version": version,
                "ownerId": owner_id,
                "availability": availability,
                "connectivityMethod": {
                    "type": connectivity_type,
                    "id": connectivity_id,
                    "name": connectivity_name
                },
                "timeouts": timeouts
            }
            return ApiCalls.api_put('/api/project-management/application', params=params)

        @staticmethod
        def post_application(_id=None, custom_id=None, name=None, description=None, version=None, owner_id=None,
                             availability=None, connectivity_type=None, connectivity_id=None, connectivity_name=None,
                             timeouts=None):
            params = {
                "id": _id,
                "customId": custom_id,
                "name": name,
                "description": description,
                "version": version,
                "ownerId": owner_id,
                "availability": availability,
                "connectivityMethod": {
                    "type": connectivity_type,
                    "id": connectivity_id,
                    "name": connectivity_name
                },
                "timeouts": timeouts
            }
            return ApiCalls.api_post('/api/project-management/application', params=params)

    class ApplicationManagement:
        @staticmethod
        def post_applications(paging_item_count=None, paging_page=None, paging_take=None, sort_column=None,
                              sort_sort=None, custom_id=None, name=None, description=None, version=None,
                              availability=None, connectivity_method=None, timeouts_from=None, timeouts_to=None,
                              owner=None, deleted=None):
            params = {
                "paging": {
                    "totalItemsCount": paging_item_count,
                    "page": paging_page,
                    "take": paging_take
                },
                "sort": {
                    "column": sort_column,
                    "sort": sort_sort
                },
                "search": {
                    "customId": custom_id,
                    "name": name,
                    "description": description,
                    "version": version,
                    "availability": availability,
                    "connectivityMethod": connectivity_method,
                    "timeouts": {
                        "from": timeouts_from,
                        "to": timeouts_to
                    },
                    "owner": owner,
                    "deleted": deleted
                }
            }
            return ApiCalls.api_post('/api/project-management/applications', params=params)

    class Account:
        @staticmethod
        def post_login(username=None, password=None):
            params = {
                "username": username,
                "password": password
            }

            return ApiCalls.api_post('/login', params=params)

    class UserManagement:
        @staticmethod
        def post_user(password='', confirm_password='', username=''):
            params = {
                "password": password,
                "confirmPassword": confirm_password,
                "username": username,
            }
            return ApiCalls.api_post('/api/user', params=params)
