from setuptools import setup

setup(
  name='kurye',
  version='0.0.1a1',
  description='simple github cloner for boilerplate projects',
  url='https://github.com/f/kurye',
  author='Fatih Kadir Akin',
  author_email='fka@fatihak.in',
  license='MIT',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
  ],
  keywords='github install clone',
  entry_points={
      'console_scripts': [
            'kurye=kurye:main',
      ],
  },
)
