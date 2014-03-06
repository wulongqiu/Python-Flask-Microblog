# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 以上三行用来解决模板中出现中文时提示unicodedecodeerror错误的问题
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname' : '乌龙球'}
    posts = [
        {
            'author' : {'nickname' : '球球'},
            'body' : '一个新的开始，一个好的开始！'
        },
        {
            'author' : {'nickname' : '大球球'},
            'body' : 'Python的Flask框架！'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)