from setuptools import setup, find_packages
 
classifiers = [
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'Operating System :: POSIX :: Linux',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.7',
  'Programming Language :: Python :: 3.8',
  'Programming Language :: Python :: 3.9'
]
 
setup(
  name='novauniverse',
  version='1.2a1',
  description='A modern API wrapper for the minecraft server "Nova Universe" written in Python.', 
  long_description=open('README.txt').read(), 
  url='https://novauniverse.net/', 
  project_urls={"Bug Tracker": "https://github.com/NovaUniverse/novauniverse.py/issues"}, 
  author='Dev Goldy', 
  author_email='jassim7256@gmail.com', 
  license='MIT', 
  classifiers=classifiers, 
  keywords=['novauniverse', 'minecraft novauniverse', 'nova universe', "mc novauniverse"], 
  packages=find_packages(), 
  install_requires=["requests"],
  python_requires=">=3.7"
)