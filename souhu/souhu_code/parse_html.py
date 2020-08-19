#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Kingsley'
__date__ = '2020/6/3'
"""
import re
from pyquery import PyQuery as pq

def parse_souhu_news(req):
    html = req.text
    d = pq(html)
    p = d('article').text()
    new_str = re.sub("[A-Za-z]", '', p)
    return new_str
