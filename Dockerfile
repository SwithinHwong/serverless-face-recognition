FROM python:3.8-slim

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y gcc g++ curl && rm -rf /var/lib/apt/lists/*
ENV PIP_INSTALL="python -m pip --no-cache-dir install --upgrade"
RUN $PIP_INSTALL numpy cython
RUN $PIP_INSTALL insightface==0.5
RUN $PIP_INSTALL onnxruntime==1.9.0
RUN python -c "from insightface.utils import download;download('models', 'buffalo_m')"

COPY demo/face_recog_demo.py /app/

WORKDIR /app

ENTRYPOINT [ "python", "face_recog_demo.py" ]
