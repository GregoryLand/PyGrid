#!/bin/bash
#exec gunicorn -k flask_sockets.worker websocket_app:app \
exec /bin/jupyter lab --ip=0.0.0.0 --port=8080 --allow-root
#"$@"
