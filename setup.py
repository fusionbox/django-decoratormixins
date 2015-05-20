import os
from setuptools import setup

version = '0.1.0'

install_requires = [
    'Django>=1.5'
]

packages = [
    'decoratormixins',
    'decoratormixins.views',
]

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(name='django-generatormixins',
      version=version,
      author='Fusinobox, Inc.',
      author_email='programmers@fusionbox.com',
      url='https://github.com/fusionbox/django-decoratormixins',
      keywords='django decorator mixin class-based-views class based views',
      description='A collection of decorator mixins for Django views.',
      long_description=read_file('README.rst'),
      classifiers=[
          'Development Status :: 1 - Planning',
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
