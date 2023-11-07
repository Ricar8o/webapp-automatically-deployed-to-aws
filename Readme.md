# webapp-automatically-deployed-to-aws


## Run App
```Bash
uvicorn app.main:app --reload
```


## Docker

```Bash
docker build -t simple-web-app .
docker run -d --name web-app-container -p 80:8000 simple-web-app
```

### Pull and Run image

```Bash
docker run -d -p 80:8000 --name simple-web-app-image-aws ricar8o/simple-webapp-fastapi
```