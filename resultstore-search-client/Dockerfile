FROM node as build-deps
WORKDIR /usr/src/app
COPY . ./
RUN yarn
RUN yarn build
EXPOSE 80
EXPOSE 3000

FROM nginx:alpine
COPY --from=build-deps /usr/src/app/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
