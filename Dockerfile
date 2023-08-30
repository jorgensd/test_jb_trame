FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y python3-pip \
    python3-dev \
    libgl1-mesa-dev \
    xvfb \
    libxrender1


RUN python3 -m pip install jupyterlab \
    jupyter \
    jupyter-book \
    jupyter-server-proxy \
    pyvista[all,trame] \
    sphinx_gallery \
    jupyterlite

EXPOSE 8888/tcp
ENV SHELL /bin/bash
# ENV PYVISTA_TRAME_SERVER_PROXY_PREFIX='/proxy/'
# ENV PYVISTA_TRAME_SERVER_PROXY_ENABLED="True"
ENV PYVISTA_BUILDING_GALLERY=True
ENV PYVISTA_OFF_SCREEN=True
ENTRYPOINT ["jupyter", "lab", "--ip", "0.0.0.0", "--no-browser", "--allow-root"]