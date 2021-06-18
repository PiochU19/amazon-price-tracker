############################
# REACT BUILD STATIC FILES #
############################

# Pull official node image

FROM node:15-alpine as builder


# Set the workdir

WORKDIR /frontend
COPY ./react/package.json ./
COPY ./react/yarn.lock ./


# Copy whole and Build

COPY ./react/ ./
RUN yarn run build



FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d

COPY --from=builder /frontend/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]