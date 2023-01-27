from setuptools import setup, find_packages
 
classifiers = [
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'Operating System :: POSIX :: Linux',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.8',
  'Programming Language :: Python :: 3.9',
  'Programming Language :: Python :: 3.10',
  'Programming Language :: Python :: 3.11'
]

import requests
readme_request = requests.get("https://raw.githubusercontent.com/NovaUniverse/NovaUniverse.py/main/README.md")
 
setup(
  name='novauniverse',
  version='2.0dev3',
  description='A modern API wrapper for the minecraft server "Nova Universe" written in Python.', 
  long_description=readme_request.text,
  long_description_content_type="text/markdown",
  url='https://novauniverse.net/', 
  project_urls={"GitHub": "https://github.com/NovaUniverse/novauniverse.py", "Bug Tracker": "https://github.com/NovaUniverse/novauniverse.py/issues"}, 
  author='Dev Goldy', 
  author_email='goldy@novauniverse.net', 
  license='MIT', 
  classifiers=classifiers, 
  keywords=['novauniverse', 'minecraft novauniverse', 'nova universe', "mc novauniverse"], 
  packages=find_packages(), 
  install_requires=open('requirements.txt').read(),
  python_requires=">=3.7"
)