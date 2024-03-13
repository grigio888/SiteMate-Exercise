FROM node:20-alpine

WORKDIR /app
COPY . /app

RUN npm install

CMD ["npm", "run", "dev", "--", "--host", "--port", "3000"]