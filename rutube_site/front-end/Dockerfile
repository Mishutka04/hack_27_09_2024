FROM node:lts-alpine
WORKDIR /front
COPY package*.json ./
RUN npm install
RUN npm install react-responsive
COPY . /front
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "dev"]