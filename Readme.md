# webapp-automatically-deployed-to-aws
El objetivo de este ejercicio es desplegar una aplicación web en varias instancias de AWS EC2 usando AWS CloudFormation. Para la construcción de la aplicación se uso el framework de Python FastApi y para facilidad a la hora de desplegar el servicio en las diferentes instancias se usó Docker.

## Conceptos

### FastApi

[FastAPI](https://fastapi.tiangolo.com/es) es un web framework moderno y rápido (de alto rendimiento) para construir APIs con Python 3.8+ basado en las anotaciones de tipos estándar de Python.

### Docker
[Docker](https://www.docker.com/) es una tecnología de creación de contenedores que permite la creación y el uso de contenedores de Linux®. Con docker, puede usar los contenedores como máquinas virtuales extremadamente livianas y modulares.

### AWS
AWS o Amazon Web Services es un proveedor de servicios en la nube, ofrece servicios de almacenamiento, de recursos de computación, de aplicaciones, bases de datos, etc.

### EC2
Amazon Elastic Compute Cloud (EC2) es un servicio de cómputo en la nube de AWS que permite a los usuarios lanzar y administrar servidores virtuales escalables, conocidos como instancias, en la nube. Estas instancias pueden ejecutar una variedad de sistemas operativos y aplicaciones, y se utilizan para alojar aplicaciones, sitios web y otros recursos informáticos en la nube.

### CloudFormation
AWS CloudFormation es un servicio de administración de infraestructura como código que permite crear y gestionar recursos de AWS de manera automatizada y predecible mediante plantillas declarativas.


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