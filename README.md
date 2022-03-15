# flask-docker-api

Flask API boilerplate with DockerFile for easy deployment.

## Tech stack

flask
wsgi (gunicorn)
nginx
docker

## Dev

```bash
source env/bin/activate
python -m flask run
```

### With WSGI server (gunicorn)

```bash
source env/bin/activate
pip install gunicorn
gunicorn --bind 0.0.0.0:5000 wsgi:app --log-level info
```