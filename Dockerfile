FROM rasa/rasa:2.0.1
COPY ./ /app
WORKDIR /app
EXPOSE 5005 5055 443
RUN rasa train