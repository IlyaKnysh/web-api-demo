from setuptools import setup, find_packages

PACKAGE_NAME = 'Demo'
PACKAGE_VERSION = '0.1'
INSTALL_REQUIRES = [
    'selene',
    'pytest',
    'allure-pytest',
    'PyHamcrest',
    'selenium',
    'pytest-xdist',
    'enum34',
    'pyodbc',
    'singleton-decorator',
    'requests',
    'jsonschema'
]
setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description=('Demo Test Project for web/api',),
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES
)
