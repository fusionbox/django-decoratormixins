import os
from setuptools import setup

version = '1.0.0'

install_requires = [
    'Django>=1.5'
]

packages = [
    'decoratormixins'
]

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(name='django-decoratormixins',
      version=version,
      author='Fusinobox, Inc.',
      author_email='programmers@fusionbox.com',
      url='https://github.com/fusionbox/django-decoratormixins',
      keywords='django decorator mixin class-based-views class based views',
      description='A collection of decorator mixins for Django views.',
      long_description=read_file('README.rst'),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries',
      ],
      install_requires=install_requires,
      packages=packages,
      license='BSD',
)
