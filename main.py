# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle

render = web.template.render('templates/')

urls = (
    '/wx', 'Handle',
    '/', 'index'
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()