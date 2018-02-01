#Docker image to test Ranger UI
#********************************
FROM ubuntu:latest 
MAINTAINER rajanikanthb@xpms.io 


#******************Running Update******************

RUN apt-get update

#***************Installing Python******************
RUN apt-get install -y python-pip
RUN apt-get install -y python3-pip
RUN apt-get -y install software-properties-common

#***************Installing Allure******************
RUN apt-add-repository ppa:qameta/allure
RUN apt-get update 
RUN apt-get install -y allure

#***************Installing wget********************

RUN apt-get install -y wget


#***************Installing Chrome ********************

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update && apt-get install -y google-chrome-unstable


#*************Installing Selenium,XLRD,Flask,Pytest,Allure Pytest,Allure Python Commons,Pytest Allure adaptor,Pytest-Xdist************

RUN pip install selenium
RUN pip install xlrd
RUN pip install Flask
RUN pip install pytest
#RUN pip install allure-pytest
RUN pip install allure-python-commons
RUN pip install pytest-allure-adaptor
RUN pip install pytest-xdist

#****************Copying Project****************

COPY PySeleniumProj/ /home/PySeleniumProj/

#***************Setting WorkDirectory***********

WORKDIR /home/PySeleniumProj/

#****************Running Project****************

RUN ["python", "/home/PySeleniumProj/LaunchRangerProj.py"]
CMD ["allure","serve","TempAllure","--port","3333"]

#***********************************************




