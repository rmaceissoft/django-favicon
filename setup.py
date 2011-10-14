from setuptools import setup, find_packages

setup(
    name='django-favicon',
    version='0.1',
    description='render favicon image from any url',
    author='Reiner Marquez',
    author_email='rmaceissoft@gmail.com',
    url='https://github.com/rmaceissoft/django-favicon',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests', 'docs']),
    classifiers=["Environment :: Web Environment",
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Framework :: Django',
                 'Topic :: Utilities'],
)