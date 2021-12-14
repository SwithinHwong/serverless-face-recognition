# FROM public.ecr.aws/lambda/python:3.8
FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.8

RUN yum update -y && yum install -y gcc gcc-c++ curl
# ENV PIP_INSTALL="pip3 --no-cache-dir install --upgrade --target \"${LAMBDA_TASK_ROOT}\""
ENV PIP_INSTALL="pip3 --no-cache-dir install --upgrade "
RUN $PIP_INSTALL numpy cython
# RUN $PIP_INSTALL insightface==0.5
# RUN $PIP_INSTALL onnxruntime==1.9.0

COPY requirements.txt  .
RUN  pip3 --no-cache-dir install -r requirements.txt

RUN echo `PWD`
RUN python -c "from insightface.utils import download;download('models', 'buffalo_m', root='/app/.insightface')"

COPY ecs/app.py /app/
COPY ecs/face_recognition_server.py /app/
COPY common /app/common
COPY data /app/data

EXPOSE 10086

WORKDIR /app

ENTRYPOINT [ "python" ]  # "/var/lang/bin/python"
# CMD ["app.py"]
CMD ["face_recognition_server.py"]
