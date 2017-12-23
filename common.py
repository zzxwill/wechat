import urllib

_ACCESS_TOKEN = '123456'
_TOKEN = 'abcdef'
_APP_ID = '123'
_APP_SECRET = 'abc'


def call_wechat_api(post_url, url_data=None):
    url_response = urllib.urlopen(url=post_url, data=url_data)
    print url_response.read()