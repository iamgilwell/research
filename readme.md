# To Start Celery `celery -A app worker -l info`
# To Demonize Celery run `celery multi start w1 -A app -l info`
        # Remember to Create 
        ## chown -R gilwell:gilwell /var/run/celery/
        ## chown -R gilwell:gilwell /var/log/celery/
# To stop the background service `celery multi stop w1 -A app -l info`