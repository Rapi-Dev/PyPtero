from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 2 - Pre-Alpha',
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='PyPtero',
  version='0.0.1a',
  description='A simple, advanced API wrapper for the Pterodactyl API',
  long_description=open('README.md', encoding='utf-8').read(),
  long_description_content_type = "text/markdown",
  url = "https://github.com/Rapi-Dev/PyPtero/", 
  project_urls={
   "Documentation": "https://github.com/Rapi-Dev/PyPtero/docs/",
   "Issues tracker": "https://github.com/Rapi-Dev/PyPtero/issues",
   },
  author='Seniatical',
  license='MIT', 
  classifiers=classifiers,
  keywords='API-Wrapper,Pterodactyl,Async,Sync', 
  packages=find_packages(),
  install_requires=['requests', 'pydantic', 'aiohttp'] 
)
