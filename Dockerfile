FROM python:3.10
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install poetry
COPY . .
RUN make install
RUN make build
ENV PATH=${PATH}:/root/.local/bin
RUN make package-install
