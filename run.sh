#!/usr/bin/env bash
sudo docker run -e DATABASE=GdgDatabase -e DATABASE_USER=GdgUser -e DATABASE_USER_PASSWORD=GdgPassword -e DATABASE_HOST=172.17.0.1 -e DATABASE_PORT=3307 -d -p 5000:5000 gdg-backend