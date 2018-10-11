import os
from setuptools import setup, find_packages

requirements = ['django==2.1', 'django_extensions==2.1.2', 'martor==1.3.0', 'Pillow==5.2.0',
                      'factory_boy==2.11.1', 'django_nose==1.4.5', 'djangorestframework==3.8.2', 'markdown==2.6.11', 'django-filter==2.0.0', 'selenium==3.14.0', 'Faker==0.9.0', 'django-selenium-login==1.0.2', 'nose==1.3.7', 'coverage==5.0a1']

if os.name == 'nt':
    requirements += ['pypiwin32', 'pywin32']

setup(
    name="INT2018",
    version="0.5.0",
    author="Jakub Szatkowski",
    author_email="jaksza18@gmail.com",
    description=("INT conference service."),
    install_requires=requirements,
    license="MiT",
    keywords="virtual scoreboard score sport",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MiT",
    ]
)
