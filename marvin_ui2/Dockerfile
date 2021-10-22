# syntax=docker/dockerfile:1
FROM node:12-alpine
RUN npm install
WORKDIR /marvin_ui2
COPY . .
#CMD ["npm", "run", "--", "ng", "serve", "--host 0.0.0.0", "--port 4200", "--disable-host-check", "--verbose"]
RUN npm run -- ng serve --host 0.0.0.0 --port 4200 --disable-host-check --verbose
