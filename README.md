:cookie: Google Cookie Jar Dumper :cookie:
==========================================

Dumps your *beloved* Google cookies in a *legacy* [cookie jar file format][1].

This file can be used with [cURL][2] or [wget][3] to authorize your HTTP calls like the following one:

```
curl -b cookies.txt https://maps.google.com/locationhistory/b/0/kml?startTime=1438380000000&endTime=1439108213113
```

Installation
------------

**Method 1**
Install directly from *pip*:

```
pip install --upgrade https://github.com/proudlygeek/google-cookies-dump/tarball/master
```

And then run from CLI with:

```
google-cookies
```

**Method 2**
If you don't want to mess up with *pip* just clone the repo:

```
git clone https://github.com/proudlygeek/google-cookies-dump.git && cd google-cookies-dump
```

And execute the command with:

```
python -m google_cookies
```

Usage
-----

```
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
```

License
-------
MIT



[1]: http://curl.haxx.se/docs/http-cookies.html#Cookies_saved_to_disk
[2]: http://curl.haxx.se/
[3]: http://www.gnu.org/software/wget/
