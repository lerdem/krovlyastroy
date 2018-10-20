# prices api for https://krovlya-stroy.dp.ua/ 

[![Travis build status](https://travis-ci.com/lerdem/krovlyastroy.svg?branch=master)](https://travis-ci.com/lerdem/krovlyastroy)

[![Django version](https://img.shields.io/badge/django-2.1.2-green.svg)](https://github.com/django/django/releases/tag/2.1.2)

### You can checkout the results [here](http://krovlya-stroy.dp.ua/kupit-profnastil-dnepr/)
### API link [here](https://krovlyastroy.pythonanywhere.com/api/)

### notes:
 - for mysqlclient
`sudo apt-get install python-dev default-libmysqlclient-dev`

- start db for dev environment
 `docker-compose up -d`

- ENV VARS for development, set that in you activate.sh file
`DEBUG=True`


### release notes:
```console
git tag -a <version_name> <release_commit_hash>
git push origin <version_name>
# on production server
git pull origin <version_name>
git reset --hard <version_name>
# ... you-deploy script
```