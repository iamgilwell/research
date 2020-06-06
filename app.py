from __future__ import absolute_import, unicode_literals
from flask import Flask 
from celery import Celery

app = Celery('jobs,data',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0',
             include=['jobs.tasks','data.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()


# app = Flask(__name__)
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'



# if __name__ == "__main__":
#     app.run(debug=True)
 