# -*- coding: utf-8 -*-
import hashlib
import web

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "Hello, this is handle view"
            signature = data.signature
            timestamp = data.timesstamp
            nonce = data.nonce
            echostr = data.echostr
            token = '9ot3rQ0xOgc'
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print("handel/GET func: hashcode, signature:", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

