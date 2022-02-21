from __future__ import absolute_import, unicode_literals
from celery import task, Celery

app = Celery('tasks', broker='redis://localhost')
app.conf.result_backend = 'redis://localhost:6379/0'  # 実行結果を保存するために追加


@task(name='liqwarpgan')
def liqwarp():
    return 