# ml_project_housing_predictor
Machine learning project
## software and account requirement

1. [GitHub Account](https://github.com/)
2. [Heroku Account](https://www.heroku.com/)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [git cli](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

## creating conda environment
```
conda activate base
conda create -p venv python==3.7 -y
```

## activating new conda environment
```
conda activate venv/
OR
conda activate venv
```

## command to install Flask
```
pip install -r requirements.txt
```

## command to install all the packages
```
pip install -e .
```

## To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

## To check the git status 
```
git status
```
## To check all version maintained by git
```
git log
```

## To create version/commit all changes by git
```
git commit -m "message"
```

## To send version/changes to github
```
git push origin main
```

## To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = anishyadav7045075175@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-regression-app

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```



```
python setup.py install
```


Install ipykernel

```
pip install ipykernel
```


Data Drift:
When your datset stats gets change we call it as data drift



## Write a function to get training file path from artifact dir