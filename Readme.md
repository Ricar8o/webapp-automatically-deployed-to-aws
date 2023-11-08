# webapp-automatically-deployed-to-aws
El objetivo de este ejercicio es desplegar una aplicación web en varias instancias de AWS EC2 usando AWS CloudFormation. Para la construcción de la aplicación se uso el framework de Python FastApi y para facilidad a la hora de desplegar el servicio en las diferentes instancias se usó Docker.

## Conceptos


## Instalando los paquetes necesarios

## Ejecutando la aplicación

### Local

```Bash
uvicorn app.main:app --reload
```

### Docker

```Bash
docker build -t simple-web-app .
docker run -d --name web-app-container -p 80:8000 simple-web-app
```

### Pull and Run Image

```Bash
docker run -d -p 80:8000 --name simple-web-app-image-aws ricar8o/simple-webapp-fastapi
```

## Definición de la plantilla