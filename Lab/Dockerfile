FROM jupyter/datascience-notebook:latest

# RUN apt-get update
# RUN apt-get --assume-yes install vim \
#     g++-aarch64-linux-gnu \
#     python3-dev

COPY requirements.txt /data/requirements.txt
#COPY requirements.txt /srv/requirements.txt
COPY MemTorch /srv/MemTorch
#COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

RUN /bin/bash -o pipefail -c "pip install -r /data/requirements.txt --no-cache"
#USER root
#RUN /bin/bash -o pipefail -c "chmod 777 /home/jovyan/shared_da"
#USER 1000
#RUN /bin/bash -o pipefail -c "cd /srv/MemTorch && python setup.py install"
#RUN /bin/bash -o pipefail -c "python setup.py install"
#RUN /bin/bash -o pipefail -c