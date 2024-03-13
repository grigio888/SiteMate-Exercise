FROM node:20-alpine

COPY . /app

WORKDIR /app
RUN npm install
RUN npm run build

COPY package.json /app/build
COPY package-lock.json /app/build
WORKDIR /app/build

RUN npm ci --omit dev

CMD [ "node", "." ]