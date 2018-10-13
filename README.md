# cspgrab

The purpose of this script is to help users better implement
Content-Security-Policy (CSP) header by identifying external sources 
a website calls out to. Implementing a CSP header is helpful in 
whitelisting external sources (script, img, font, etc.), thus reducing
the risk of experiencing cross-site scripting (XSS).

## Requirements
```
$ pip install -r requirements.txt
```

## Usage
For python2.x:
```
$ python cspgrab.py -u [url]
```

For python3.x:
```
$ python3 cspgrab.py -u [url]
```