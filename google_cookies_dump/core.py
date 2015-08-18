#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Google Cookie Dump.

Usage:
    google-cookies --email=<email> --password=<password> [--cookie_name=<cookie_name>]
    google-cookies -h | --help
    google-cookies --version

Options:
    -h --help                   Shows this screen.
    --version                   Show version.
    --email=EMAIL               Google account's name (e.g. example@gmail.com)
    --password=PASSWORD         Google account's password
    --cookie_name=COOKIE_NAME   Output cookie file [default: cookiejar]
"""
import google_cookies_dump
from docopt import docopt
from cookie import GoogleCookie

def main():
    arguments = docopt(__doc__, version="Google Auth Cookie Dumper version %s" % google_cookies_dump.__version__)
    google_cookie = GoogleCookie(email=arguments['--email'],
                                 password=arguments['--password'],
                                 cookie_file=arguments['--cookie_name'])
    google_cookie.run()
