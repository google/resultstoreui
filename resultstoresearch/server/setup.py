from setuptools import setup, find_packages

setup(name='resultstoresearch',
      version='0.1',
      description='Server for resultstoresearch',
      url='https://github.com/google/resultstoreui',
      author='Craig Lewis',
      author_email='lewiscraig@google.com',
      license='MIT',
      packages=find_packages(include=['resultstoresearch.*']),
      zip_safe=False)
