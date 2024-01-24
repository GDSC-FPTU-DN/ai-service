<div style="width:100%;display:flex;flex-direction:column;justify-content:center;align-items:center">
<img style="width:80px"
src="https://seeklogo.com/images/G/google-developers-logo-F8BF3155AC-seeklogo.com.png" alt="logo"/>
</div>
<h3 style="text-align:center">Google Developer Student Clubs - FPT University Da Nang</h3>

# AI Services

![version](https://img.shields.io/badge/version-0.1.1-green)
![release](https://img.shields.io/badge/release-0.1.0-blue)

## ✨ Available Services

## ⏩ Forwarding Server

The forwarding server help adding children server for processing. The parent server acts as a controller for load balancing.

```bash
# Specifying forwarding server by query params `fw`
curl --location 'https://{api-endpoint}/?fw=0' --request 'POST'

# Auto forwarding server. The parent server will controll loading balance among registered servers.
curl --location 'https://{api-endpoint}/?fw=auto' --request 'POST'
```

- Get all registered forwarding servers.

```bash
curl --location 'https://{domain}/service/fw/' --request 'GET'
```

- Register forwarding server.

```bash
curl --location 'https://{domain}/service/fw/' --request 'POST' --data '{"url":"{children-base-domain}"}'
```

- Delete forwarding server.

```bash
curl --location 'https://{domain}/service/fw/' --request 'DELETE' --data '{"index":0}'
```

### Server Health Checker

```bash
curl --location '{children-base-domain}/health'
```

This route checks the health status of children server. The children is considered as good health when it return anything with status 200.

### Children Server Endpoint Request & Response

- `/api/rembg/`

```json
// Request. Form-data
{
    "image": "<image-data>"
}

// Response. JSON
{
    "data": {
        "image": "<static-access-url>"
    }
}
```

- `/api/fd/`

```json
// Request. Form-data
{
    "image": "<image-data>"
}

// Response. JSON
{
    "data": {
        "faces": FaceObject[]
    }
}

// FaceObject
{
    "bbox": {
        "x": 0,
        "y": 0,
        "width": 100,
        "height": 100
    }
}
```

- `/api/chats/`

```json
// Request. JSON
{
    "prompt": "A Prompt from user"
}

// Response. JSON
{
    "data": {
        "message": "A Message from AI"
    }
}
```

- `/api/chats/:id`

```json
// Request. JSON
{
    "prompt": "A Prompt from user",
    "conversation": [
        {
            "role": "user",
            "content": "Message A"
        },
        {
            "role": "assistant",
            "content": "Message B"
        }
    ]
}

// Response. JSON
{
    "data": {
        "message": "A Message from AI"
    }
}
```

- `/api/img2text/`

```json
// Request. Form-data
{
    "image": <image-data>
}

// Response. JSON
{
    "data": {
        "caption": "Caption of image"
    }
}
```

## 😊 Contributors

- GDSC-FPTU [[gdsc-fptu](https://github.com/gdsc-fptu)]
- Đoàn Quang Minh [[Ming-doan](https://github.com/Ming-doan)]
