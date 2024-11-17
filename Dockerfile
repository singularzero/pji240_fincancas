FROM python:alpine
LABEL authors="fe"

ARG PORTA
ENV PORTA $PORTA
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
EXPOSE ${PORTA}/tcp
ENTRYPOINT ["./run.sh"]