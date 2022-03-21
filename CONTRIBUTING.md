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
docker run --rm -it pashkatrick/calendario
```

### Sources and docker

Clone  repository
```
git clone https://github.com/pashkatrick/randomcofffee.git
```

Go into repository folder
```
cd randomcofffee
```

Build [Dockerfile](/Dockerfile) with specific tag as like:
```
docker build -t rc-api .
```

Run docker container
```
docker run --rm -it -p 5000:5000/tcp rc-api
```

Check ```localhost:5000``` in your browser, should be:   

![image](https://user-images.githubusercontent.com/8003175/153649879-993e1f36-366c-47ac-a052-c47417d7f915.png)

Open [postman-colllection](/postman-collection.json) via Postman and set mock data to database with ```__utils__/bootstrap``` request

![image](https://user-images.githubusercontent.com/8003175/153650107-9519368d-82ca-4dcf-8243-d81ef5d44c5b.png)

That's it, enjoy!
