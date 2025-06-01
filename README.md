# ats-track

A REST API for candidate tracking in an ATS system. 

# Requirements
```
$ postgres --version
> postgres (PostgreSQL) 17.4 (Debian 17.4-1.pgdg120+2)
```

# Setup

Start postgres db

```bash
docker-compose up -d
```

Run migrate
```bash
python manage.py migrate
```

Start server

```bash
python manage.py runserver
```

# Usage

## Create Candidate
POST http://127.0.0.1:8000/api/v1/ats/candidate/
sample request data 
```json
{
    "name": "Ajay Kumar yadav",
    "age": 20,
    "gender": "M",
    "email": "ajaykumaryadav@gmail.com",
    "phone_number": "9876543211",
}
```

Example cURL request
```bash
curl -s -X POST http://127.0.0.1:8000/api/v1/ats/candidate/ \
    -H 'content-type: application/json' \
    -d '{"name": "John doe", "age": 20, "gender": "M", "email": "johndoe@gmail.com", "phone_number": "9876643211"}' | jq
```

## Update Candidate
PATCH http://127.0.0.1:8000/api/v1/ats/candidate/<candidate_id>/
sample request data
```json
{
    "age": 21,
    "phone_number": "9876543223",
}
```
Example cURL request
```bash
curl -s -X PATCH http://127.0.0.1:8000/api/v1/ats/candidate/<id>/ \
    -H 'content-type: application/json' \
    -d '{"age": 21, "phone_number": "9876543223"}' | jq
```

## List Candidates
GET http://127.0.0.1:8000/api/v1/ats/candidate/

Example cURL request

```bash
curl http://127.0.0.1:8000/api/v1/ats/candidate/ | jq
```

## Search Candidates by name

POST http://127.0.0.1:8000/api/v1/ats/candidate/search/
sample request data
```json
{
    "name": "Ajay Kumar yadav",
}
```
Example cURL request
```bash
curl -s -X POST http://127.0.0.1:8000/api/v1/ats/candidate/search/ \
    -H 'content-type: application/json' \
    -d '{"name": "Ajay Kumar Yadav"}' | jq
```