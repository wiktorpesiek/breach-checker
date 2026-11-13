# Zadanie 3 – Wiktor Pesiek

1. Etykiety i pochodzenie warstw
1a. docker inspect
{"autor":"Wiktor Pesiek","data":"2026-11-06","maintainer":"Wiktor Pesiek"}

1b. docker history wiktor-frontend:v1
IMAGE          CREATED              CREATED BY                                      SIZE      COMMENT
6673fae4aca1   About a minute ago   EXPOSE [80/tcp]                                 0B        buildkit.dockerfile.v0
<missing>      About a minute ago   RUN /bin/sh -c htmlhint /usr/share/nginx/htm…   4.1kB     buildkit.dockerfile.v0
<missing>      About a minute ago   COPY . /usr/share/nginx/html # buildkit         36.9kB    buildkit.dockerfile.v0
<missing>      7 minutes ago        RUN /bin/sh -c apk add --no-cache nodejs npm…   99.3MB    buildkit.dockerfile.v0
<missing>      7 minutes ago        LABEL autor=Wiktor Pesiek data=2026-11-06       0B        buildkit.dockerfile.v0
<missing>      7 minutes ago        LABEL maintainer=Wiktor Pesiek                  0B        buildkit.dockerfile.v0
<missing>      2 weeks ago          RUN /bin/sh -c set -x     && apkArch="$(cat …   52.4MB    buildkit.dockerfile.v0
<missing>      2 weeks ago          ENV ACME_VERSION=0.4.1                          0B        buildkit.dockerfile.v0
<missing>      2 weeks ago          ENV NJS_RELEASE=1                               0B        buildkit.dockerfile.v0
<missing>      2 weeks ago          ENV NJS_VERSION=1.0.2                           0B        buildkit.dockerfile.v0
<missing>      2 weeks ago          CMD ["nginx" "-g" "daemon off;"]                0B        buildkit.dockerfile.v0
<missing>      2 weeks ago          STOPSIGNAL SIGQUIT                              0B        buildkit.dockerfile.v0
<missing>      2 weeks ago          EXPOSE map[80/tcp:{}]                           0B        buildkit.dockerfile.v0
<missing>      2 weeks ago          ENTRYPOINT ["/docker-entrypoint.sh"]            0B        buildkit.dockerfile.v0
<missing>      2 weeks ago          COPY 30-tune-worker-processes.sh /docker-ent…   16.4kB    buildkit.dockerfile.v0
<missing>      2 weeks ago          COPY 20-envsubst-on-templates.sh /docker-ent…   12.3kB    buildkit.dockerfile.v0
<missing>      2 weeks ago          COPY 15-local-resolvers.envsh /docker-entryp…   12.3kB    buildkit.dockerfile.v0
<missing>      2 weeks ago          COPY 10-listen-on-ipv6-by-default.sh /docker…   12.3kB    buildkit.dockerfile.v0
<missing>      2 weeks ago          COPY docker-entrypoint.sh / # buildkit          8.19kB    buildkit.dockerfile.v0
<missing>      2 weeks ago          RUN /bin/sh -c set -x     && addgroup -g 101…   5.75MB    buildkit.dockerfile.v0
<missing>      2 weeks ago          ENV DYNPKG_RELEASE=1                            0B        buildkit.dockerfile.v0
<missing>      2 weeks ago          ENV PKG_RELEASE=1                               0B        buildkit.dockerfile.v0
<missing>      2 weeks ago          ENV NGINX_VERSION=1.31.8                        0B        buildkit.dockerfile.v0
<missing>      2 weeks ago          LABEL maintainer=NGINX Docker Maintainers <d…   0B        buildkit.dockerfile.v0
<missing>      2 weeks ago          CMD ["/bin/sh"]                                 0B        buildkit.dockerfile.v0
<missing>      2 weeks ago          ADD alpine-minirootfs-3.24.3-x86_64.tar.gz /…   9.08MB    buildkit.dockerfile.v0

1c. Odpowiedź



2. RUN działa raz
2a. - czas 8082 i czas 8081 
Fri Nov  6 13:31:12 UTC 2026
Fri Nov  6 13:31:12 UTC 2026

2b. 
CONTAINER ID   IMAGE                COMMAND                  CREATED              STATUS              PORTS                                     NAMES
c6b28fd25b76   wiktor-frontend:v2   "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8082->80/tcp, [::]:8082->80/tcp   z2b
2647c6bf011e   wiktor-frontend:v2   "/docker-entrypoint.…"   3 minutes ago        Up 3 minutes        0.0.0.0:8081->80/tcp, [::]:8081->80/tcp   z2a
df6bba0fac43   nginx                "/docker-entrypoint.…"   21 minutes ago       Up 21 minutes       0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   mojkontener

3. Nadpisanie CMD

        root   /usr/share/nginx/html;
        root   /usr/share/nginx/html;
    #    root           html;
    # deny access to .htaccess files, if Apache's document root