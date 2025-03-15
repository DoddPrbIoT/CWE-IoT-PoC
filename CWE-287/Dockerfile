FROM node:20.13-alpine
WORKDIR /home/node
COPY . .
RUN npm install
EXPOSE 3000
CMD [ "npm", "run", "start" ]