from distutils.core import setup
import google_cookies


install_requires = [
    'requests==2.7.0',
    'docopt==0.6.2'
]

setup(name='google_cookies_dump',
      version=google_cookies.__version__,
      description=google_cookies.__doc__.strip(),
      author=google_cookies.__author__,
      author_email='g.bargelli@gmail.com',
      download_url='https://github.com/proudlygeek/google-cookies-dump',
      install_requires=install_requires,
      entry_points = {
          'console_scripts': [
              ['google-cookies = google_cookies.__main__:main']
          ]
      }
)
