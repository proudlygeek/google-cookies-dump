# -*- coding: utf-8 -*-

import os
import re
import docopt
import requests
from docopt import docopt
from cookielib import Cookie, MozillaCookieJar

class GoogleCookie:
    def __init__(self, email, password, cookie_file):
        self.email = email
        self.password = password
        self.session = requests.Session()
        self.session.cookies = MozillaCookieJar(cookie_file)

    def scrapeGALX(self):
        r = requests.get('https://accounts.google.com/ServiceLogin')
        galx = re.compile('.*\\s*name="GALX"\\s*.*\\s*value="(?P<galx>[a-zA-Z0-9_-]+)">')
        match = galx.search(r.text)

        if not match:
            raise Exception('Cannot parse GALX out of login page')

        return match.group('galx')

    def makeCookie(self, name, value):
        return Cookie(
            version=0,
            name=name,
            value=value,
            port=None,
            port_specified=False,
            domain=".google.com",
            domain_specified=True,
            domain_initial_dot=True,
            path="/",
            path_specified=True,
            secure=False,
            expires=None,
            discard=False,
            comment=None,
            comment_url=None,
            rest=None
        )

    def run(self):
        data = {
          'GALX': self.scrapeGALX(),
          'Email': self.email,
          'Passwd': self.password,
          'PersistentCookie': "yes",
        }

        if not os.path.exists('cookiejar'):
            print "Auth cookies..."
            self.session.cookies.save()
            self.session.post("https://accounts.google.com/ServiceLoginAuth", data=data)
        else:
            print "Auth cookies already present, skipping..."

        print "Retrieving cookies"
        self.session.cookies.load()
        self.session.cookies.set_cookie(self.makeCookie('GALX', data['GALX']))
        self.session.post("https://accounts.google.com/ServiceLoginAuth", data=data)

        self.session.cookies.save(ignore_discard=True)
        print "...done!"
