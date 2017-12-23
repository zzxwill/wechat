# -*- coding: utf-8 -*-
import hashlib
import web
import common
import receive
import reply

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
            token = common._TOKEN
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

    def POST(self):
        try:
            web_data = web.data()
            print("Handle Post webdata is ", web_data)

            receive_message = receive.parse_xml(web_data)
            if isinstance(receive_message, receive.Msg) and receive_message.message_type == 'text':
                to_user = receive_message.from_user_name
                from_user = receive_message.to_user_name
                content = 'test'
                reply_message = reply.TextMsg(toUserName=to_user, fromUserName=from_user, content=content)
                return reply_message.send()
            else:
                print('暂不处理')
                return 'success'
        except Exception, Argment:
            return Argment


