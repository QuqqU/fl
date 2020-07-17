#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, Response

app = Flask(__name__)
app.config['server_name'] = 'example.com:5000'

@app.route("/")
def helloworld():
    res = Response("test for res")
    res.headers.add('program-name', 'the second flask book')
    res.set_data("eeeeeeeeeeeboooooooooook")
    res.set_cookie("accccesslevel", 'efe')
    print(res.get_data())
    return res



@app.route("/h", host="example2.com")
def helloworld2():
    return "hello world2~"

@app.route("/re", redirect_to="/board")
def red():
    return "redirect"

@app.route("/board", methods=['GET'])
def board_list_get():
    return "12344"

@app.route("/board", methods=['post'])
def board_list_post():
    return "456"


@app.route("/board/ex/", defaults={ "appaarticle_idx" : 1234567890 })
@app.route("/board/<appaarticle_idx>")
def board_view(appaarticle_idx):
    return "----{num}----".format(num=appaarticle_idx)


