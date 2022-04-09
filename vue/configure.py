# -*- coding: utf-8 -*-

"""
@author: kn
@software: PyCharm
@file: configure.py
@time: 2022/4/3 17:26
"""
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from concurrent.futures import ThreadPoolExecutor
from vue.jobs import job1,job2

class SchedulerConfig(object):
    # 持久化配置，数据持久化至sqlite
    SCHEDULER_JOBSTORES = {'default': SQLAlchemyJobStore(url='sqlite:///jobstores.db')}
    # 线程池配置，最大20个线程
    #SCHEDULER_EXECUTORS = {'default': ThreadPoolExecutor(20)}
    # 调度开关开启
    SCHEDULER_API_ENABLED = True
    # 设置容错时间为 1小时
    SCHEDULER_JOB_DEFAULTS = {'misfire_grace_time':3600}
    # 配置时区
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'

    JOBS = [
        {
            'id': 'ertyuio234',
            'name': 'job1',
            'func': job1,
            'trigger': 'interval',
            #'start_date': '2021-01-27 13:31:00',
            #'end_date': '2021-01-27 13:33:00',
            'seconds': 60,
            'replace_existing': True  # 重新执行程序时，会将jobStore中的任务替换掉
        },
        {
            'id': 'job2',
            'name': 'job2',
            'func': job2,
            'trigger': 'interval',
            #'start_date': '2021-01-27 13:31:00',
            #'end_date': '2021-01-27 13:33:00',
            'seconds': 60,
            'replace_existing': True  # 重新执行程序时，会将jobStore中的任务替换掉
        }
    ]

