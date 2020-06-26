FROM node as build-deps
WORKDIR /usr/src/app
COPY . ./

ARG REACT_APP_CLIENT_ID
ENV REACT_APP_CLIENT_ID=$REACT_APP_CLIENT_ID

ARG REACT_APP_PROJECT_ID
ENV REACT_APP_PROJECT_ID=$REACT_APP_PROJECT_ID

ARG REACT_APP_DESTINATION_ADDRESS
ENV REACT_APP_DESTINATION_ADDRESS=$REACT_APP_DESTINATION_ADDRESS

RUN yarn
RUN yarn build
EXPOSE 80
EXPOSE 3000

FROM nginx:alpine
COPY --from=build-deps /usr/src/app/build /usr/share/nginx/html
COPY --from=build-deps /usr/src/app/nginx.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]

# For Local Development
# CMD ["yarn", "start"]
