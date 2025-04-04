rabbitmqctl list_queues
rabbitmqadmin get queue_name count=1 requeue=false
rabbitmqadmin get celery count=1 requeue=false
rabbitmqadmin get celery count=1 requeue=false
ERROR: Argument "celery" not in the name=value format
rabbitmqadmin get queue=celery count=1 requeue=false
rabbitmqadmin get queue=celery count=1 ackmode=reject
docker network ls
exit
rabbitmqadmin get queue=celery count=1 requeue=false
rabbitmqadmin get queue=celery count=1 ackmode=reject
docker inspect rabbitmq
exit
rabbitmqadmin get queue=celery count=1 ackmode=requeue 
rabbitmqadmin get queue=celery count=1 ackmode=reject-requeue-true
exit
rabbitmqadmin get queue=celery count=1 ackmode=reject
docker logs kozhev-rabbitmq-1
exit
