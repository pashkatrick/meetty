# Calendario

## Get Started 🚀

 - [docker](#docker-only)
 - [sources](#sources-and-docker)

### Requirements

 - [git](https://git-scm.com/downloads)
 - [docker](https://docs.docker.com/get-docker/)
 - [postman](https://www.postman.com/downloads/)


### Docker only

before the start you need 
```
docker pull pashkatrick/calendario
```
and then 
```
docker run --rm -it -p 5000:5000 pashkatrick/calendario
```

to open docs -> move to localhost:5000/docs and wait for a swagger

<p align="left">
<img width="600" alt="screenshot" src="https://user-images.githubusercontent.com/8003175/162046377-b6b69bda-8782-4ad1-aa21-3cfe9fdb8bf0.jpg">
</p>

### Sources and docker

Clone  repository
```
git clone https://github.com/pashkatrick/calendario.git
```

Go into repository folder
```
cd calendario
```

Build [Dockerfile](/Dockerfile) with specific tag as like:
```
docker build -t calendario .
```

Run docker container
```
docker run --rm -it -p 5000:5000 pashkatrick/calendario
```

Check ```localhost:5000``` in your browser, should be:   

![image](https://user-images.githubusercontent.com/8003175/153649879-993e1f36-366c-47ac-a052-c47417d7f915.png)

That's it, enjoy!
