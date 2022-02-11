# Contributing Random Coffee 

## Get Started 🚀

### Requirements

 - [git](https://git-scm.com/downloads)
 - [docker](https://docs.docker.com/get-docker/)
 - [postman](https://www.postman.com/downloads/)

### Setup

Clone  repository
```
git clone https://github.com/pashkatrick/randomcofffee.git
```

Go into repository folder
```
cd randomcofffee
```

Build Dockerfile with specific tag as like:
```
docker build -t rc-api .
```

Run docker container
```
docker run --rm -it -p 5000:5000/tcp rc-api
```

Check ```localhost:5000``` in your browser, should be: 


Open [postman-colllection](/postman-collection.json) via Postman

Set mock data to database with ```__utils__/bootstrap``` request

That's it! 
