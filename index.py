# -*- coding: utf-8 -*-
import hashlib
import web
import common
import receive
import reply

class Index(object):
    render = web.template.render('templates/')

    def GET(self):
        return self.render.index

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


