A slack bot example program made with python.

# If you get an SSL error, please install the SSL related package.
```
/usr/local/lib/python2.7/dist-packages/requests/packages/urllib3/util/ssl_.py:122: 
InsecurePlatformWarning: A true SSLContext object is not available.
This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail.
You can upgrade to a newer version of Python to solve this. For more information, 
see https://urllib3.readthedocs.io/en/latest/security.html#insecureplatformwarning.
InsecurePlatformWarning
```

```
pip install pyOpenSSL ndg-httpsclient pyasn1
```
Reference: https://www.franzoni.eu/python-requests-ssl-and-insecureplatformwarning/
