# -*- coding: utf-8 -*-

"""
@author: kn
@software: PyCharm
@file: app.py
@time: 2022/4/3 17:19
"""
import os
from dotenv import load_dotenv
from vue import createapp

dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.flaskenv')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = createapp()

if __name__ == "__main__":
    app.run()