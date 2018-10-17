# datascience
attempts related to data reading,writing,cleaning,parsing,visualisation using machine learning libraries

# Requirements
### Python3
```sh 
$ cd Desktop
$ sudo apt-get install python3
$ sudo apt-get install jupyter-notebook
$sudo apt-get install python3-pip
$pip3 install pandas
$pip3 install xlwt
```

# USE CASE
### passing data from a html page to database and writing the obtained data to an excel file  using python-flask
```sh
$ pip3 install flask
$ cd datascience
$ mkdir formdata_to_xl
$ cd formdata_to_xl
$ mkdir template
$ vim index.html
$ cd..
$ vim __init__.py
$ chmod +x __init__.py
```

# SERVICES	
### Start mariadb service
```sh
$ systemctl enable --now mariadb.service
```
# lbph
### create folder trainingimages and place at least 2 images in it for training dataset
### run the program as

```sh
$ cd lbph
$ chmod +x recognize.py
$ ./recognize --training ./trainingimages --testing ./testingimages
```

