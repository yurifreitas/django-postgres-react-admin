FROM node:16-alpine
WORKDIR /app
COPY . /app
ENV PATH /app/node_modules/.bin:$PATH
RUN npm install

EXPOSE 3000
CMD ["npm", "start"]