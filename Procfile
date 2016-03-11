web: bench serve
longjob_worker: sh -c 'cd sites && exec ../env/bin/python -m frappe.celery_app -n longjobs@%h worker'
redis_async_broker: redis-server config/redis_async_broker.conf
socketio: /usr/local/bin/node apps/frappe/socketio.js
workerbeat: sh -c 'cd sites && exec ../env/bin/python -m frappe.celery_app beat -s scheduler.schedule'
worker: sh -c 'cd sites && exec ../env/bin/python -m frappe.celery_app worker'
async_worker: sh -c 'cd sites && exec ../env/bin/python -m frappe.celery_app -n async@%h worker'
redis_cache: redis-server config/redis_cache.conf