FROM python:3.7-alpine 
RUN apk update \ 
&& apk add busybox-extras \
&& rm -rf /var/cache/apk/* \
&& pip install pika \
&& mkdir -p /src/deploy
WORKDIR /src/deploy
COPY ThesisWork .
CMD ["/bin/sh"]

