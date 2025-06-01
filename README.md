# ats-track

A REST API for candidate tracking in an ATS system. 

# Requirements
```
$ postgres --version
> postgres (PostgreSQL) 17.4 (Debian 17.4-1.pgdg120+2)
```

# Setup

start postgres db

```bash
docker-compose up -d
```

run migrate
```bash
python manage.py migrate
```

start server

```bash
python manage.py runserver
```

# Usage

