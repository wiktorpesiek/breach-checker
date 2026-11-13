FROM nginx:alpine
LABEL maintainer="Wiktor Pesiek"
LABEL autor="Wiktor Pesiek" data="2026-11-06"
RUN apk add --no-cache nodejs npm && npm install -g htmlhint
COPY . /usr/share/nginx/html
RUN htmlhint /usr/share/nginx/html/index.html
RUN date > /usr/share/nginx/html/build.txt
EXPOSE 80