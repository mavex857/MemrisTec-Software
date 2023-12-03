FROM jupyterhub/jupyterhub:latest

RUN pip install --no-cache \
    oauthenticator \
    dockerspawner \
    jupyterhub-nativeauthenticator

RUN apt-get update
RUN apt-get --assume-yes install vim \
    g++-aarch64-linux-gnu \
    python3-dev

COPY requirements.txt /srv/data/requirements.txt
# COPY requirements.txt /srv/requirements.txt
# COPY MemTorch /srv/MemTorch
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
COPY script.py /srv/data/my_shared_folder/script.py
WORKDIR /srv/jupyterhub

#VOLUME /srv/jupyterhub/shared_data
#VOLUME /srv/jupyterhub/data
#RUN  777 /srv/jupyterhub/shared_data

# RUN pip install -r /srv/jupyterhub/requirements.txt
# RUN cd /srv/MemTorch && python setup.py install && cd ~

