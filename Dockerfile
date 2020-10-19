FROM rasa/rasa:1.10.10
COPY ./ /app
WORKDIR /app
EXPOSE 5005 5055
RUN rasa train