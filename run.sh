#!/bin/bash

ACT_PATH=$(pwd)

docker run -v "$ACT_PATH/assets:/app/assets" -v "$ACT_PATH/output:/app/output" -e DATABASE=GdgDatabase -e DATABASE_USER=GdgUser -e DATABASE_USER_PASSWORD=GdgPassword -e DATABASE_HOST=172.17.0.1 -e DATABASE_PORT=3307 -d -p 5000:5000 gdg-backend