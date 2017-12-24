import urllib

_ACCESS_TOKEN = '123456'
_TOKEN = 'R423jf8URWQPVN9uy'
_APP_ID = 'wx128b565bd6f7e1ff'
_APP_SECRET = '68a7df087bd7f1346cb4139ade2805cb'


def call_wechat_api(post_url, url_data=None):
    url_response = urllib.urlopen(url=post_url, data=url_data)
    print url_response.read()