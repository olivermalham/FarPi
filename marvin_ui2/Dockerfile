# syntax=docker/dockerfile:1
#FROM node:12-alpine
#RUN npm install
#WORKDIR /marvin_ui2
#COPY . .
#CMD ["npm", "run", "--", "ng", "serve", "--host 0.0.0.0", "--port 4200", "--disable-host-check", "--verbose"]
#RUN npm run -- ng serve --host 0.0.0.0 --port 4200 --disable-host-check --verbose

FROM node:14.15.0

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json
RUN npm install
RUN npm install -g @angular/cli@10.2.0


COPY . /app

CMD npm start