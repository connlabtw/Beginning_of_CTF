From python:latest

RUN apt update && apt install -y vim git netcat 

# install pip pwntools crypto for python2
RUN apt install -y  python-pip 
RUN pip2 install --upgrade pwntools crypto

# install pwntools crypto for python3
RUN pip3 install --upgrade pip crypto
RUN pip3 install git+https://github.com/arthaud/python3-pwntools.git

COPY homework /root/
COPY lab /root/
