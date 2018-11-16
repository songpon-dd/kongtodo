# Kongfig

POC Service for Knog auto configure testing.

## APIs

**List all todo**

    GET /v1/todos

**Get todo by id**

    GET /v1/todos/<id>

**Create new todo**

    POST /v1/todos

with payload:

    { 
		"title": "create todo app",
		"description": "Create todo app for test on kong"
	}

**Update todo**

    PUT /v1/todos/<id>
with payload:

    { 
		"title": "updating todo",
		"description": "updating something"
	}

**Delete todo**

    DELETE /v1/todos/<id>
