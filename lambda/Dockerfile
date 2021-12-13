# FROM public.ecr.aws/lambda/python:3.8
FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.8

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

# Copy function code
COPY lambda/app.py ${LAMBDA_TASK_ROOT}
COPY common/dao.py ${LAMBDA_TASK_ROOT}
COPY common/face_detection.py ${LAMBDA_TASK_ROOT}
COPY common/face_match.py ${LAMBDA_TASK_ROOT}
COPY common/face_recognition.py ${LAMBDA_TASK_ROOT}
COPY data ${LAMBDA_TASK_ROOT}/data

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]
