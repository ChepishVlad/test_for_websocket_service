FROM ubuntu

COPY ./app /app

WORKDIR /app

EXPOSE 4000

RUN ["chmod", "+x", "./tester.so"]
CMD ./tester.so 0.0.0.0 4000
