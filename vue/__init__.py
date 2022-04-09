# -*- coding: utf-8 -*-

"""
@author: kn
@software: PyCharm
@file: __init__.py.py
@time: 2022/4/3 17:25
"""
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from flask import Flask,url_for,jsonify,render_template
from flask_apscheduler import APScheduler
from vue.configure import SchedulerConfig

def createapp():
    app = Flask(__name__)
    scheduler = APScheduler()
    # 导入定时器配置
    app.config.from_object(SchedulerConfig())
    # 初始化定时器
    scheduler.init_app(app)
    # 启动定时器，默认后台启动了
    scheduler.start()
    # 启动flask
    app.run()

    @app.route('/',methods=['GET'])
    def index():
        return render_template('index.html')

    @app.route('/jobs',methods=['GET'])
    def jobs():
        #data = requests.get('http://127.0.0.1:7001/' + url_for('scheduler.get_jobs'))
        #print(data)
        data = [1,2,3]
        return jsonify(
            {
                "status":"success",
                "data":data
            }
        )

    @app.route('/jobpause/<job_id>',methods=['GET'])
    def jobpause_test(job_id):
        return scheduler.pause_job(id=job_id, jobstore="default")

    @app.route('/jobresume/<job_id>',methods=['GET'])
    def jobresume_test(job_id):
        return scheduler.resume_job(id=job_id, jobstore="default")

    @app.route('/jobremove/<job_id>',methods=['GET'])
    def jobremove_test(job_id):
        return scheduler.remove_job(id=job_id, jobstore="default")

    return app