from setuptools import setup, find_packages
 
classifiers = [
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.8'
]
 
setup(
  name='novauniverse',
  version='1.0a5',
  description='A modern API wrapper for the minecraft server Nova Universe written in Python.', 
  long_description=open('README.txt').read(), 
  url='https://novauniverse.net/', 
  project_urls={"Bug Tracker": "https://github.com/NovaUniverse/novauniverse.py/issues"}, 
  author='Dev Goldy', 
  author_email='jassim7256@gmail.com', 
  license='MIT', 
  classifiers=classifiers, 
  keywords=['novauniverse', 'minecraft novauniverse', 'nova universe'], 
  packages=find_packages(), 
  install_requires=["requests"],
  python_requires=">=3.7"
)