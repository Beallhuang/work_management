nohup /home/huang.biao/anaconda3/envs/django/bin/python -m uvicorn belle_management.asgi:application --host 0.0.0.0 --port 8002 > /dev/null 2>&1 & 
# 输出pid到文件
echo $! > /home/huang.biao/http_app/Django/belle_management/run_socket.pid