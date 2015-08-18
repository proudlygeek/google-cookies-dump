from setuptools import setup, find_packages
import google_cookies_dump


install_requires = [
    'requests==2.7.0',
    'docopt==0.6.2'
]

setup(name='google_cookies_dump',
      version=google_cookies_dump.__version__,
      description=google_cookies_dump.__doc__.strip(),
      author=google_cookies_dump.__author__,
      author_email='g.bargelli@gmail.com',
      download_url='https://github.com/proudlygeek/google-cookies-dump',
      packages=find_packages(),
      py_modules=['google_cookies_dump'],
      install_requires=install_requires,
      entry_points = {
          'console_scripts': [
              ['google-cookies = google_cookies_dump.__main__:main']
          ]
      }
)
