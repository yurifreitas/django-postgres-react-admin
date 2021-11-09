FROM nginx:alpine
WORKDIR /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY dev.conf /etc/nginx/conf.d/
EXPOSE 80