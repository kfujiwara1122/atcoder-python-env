ARG PYTHON_VERSION
ARG PYPY_VERSION

FROM pypy:${PYTHON_VERSION}-${PYPY_VERSION}-slim

ARG HOME_DIR

ENV HOME=${HOME_DIR}
WORKDIR ${HOME_DIR}
COPY requirements.txt ${HOME_DIR}/

RUN apt-get update && apt-get install -y \
    git; \
    pip3 install --no-cache-dir -r requirements.txt
