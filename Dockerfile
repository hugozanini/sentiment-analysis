FROM python:3.8-slim-buster
WORKDIR /api
#ENV TZ=America/sao_paulo

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

#Downloading pre-trained model from google drive
RUN mkdir -p ./assets \
    && gdown --id $MODEL_ID -O assets/best_model_state.bin

#CMD ["echo", "Running Sentiment Analysis API"]
CMD ["bin/start_server"]
