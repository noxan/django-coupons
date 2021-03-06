import os
from setuptools import setup, find_packages

import coupons


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-coupons',
    version=coupons.__version__,
    description='A reuseable Django application for coupon gereration and handling.',
    long_description=read('README.md'),
    license=read('LICENSE'),
    author='byteweaver',
    author_email='contact@byteweaver.net',
    url='https://github.com/byteweaver/django-coupons',
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    tests_require=[
        'django-nose',
        'coverage',
        'django-coverage',
    ],
    test_suite='coupons.tests',
)
