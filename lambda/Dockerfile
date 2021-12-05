FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.8

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

RUN yum update -y && yum install -y gcc gcc-c++ curl
# ENV PIP_INSTALL="pip3 --no-cache-dir install --upgrade --target \"${LAMBDA_TASK_ROOT}\""
ENV PIP_INSTALL="pip3 --no-cache-dir install --upgrade "
RUN $PIP_INSTALL numpy cython
# RUN $PIP_INSTALL insightface==0.5
# RUN $PIP_INSTALL onnxruntime==1.9.0

COPY requirements.txt  .
RUN  pip3 --no-cache-dir install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

RUN echo `PWD`
RUN python -c "from insightface.utils import download;download('models', 'buffalo_m', root='./.insightface')"

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]
