#!/bin/bash

# 启动 Uvicorn 服务器
echo "Starting Uvicorn server..."

# 确保静态文件已收集
python3 manage.py collectstatic --noinput

# 启动 Uvicorn
uvicorn config.wsgi:application --host 0.0.0.0 --port 8000 --reload