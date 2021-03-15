FROM python:3.8-slim-buster
WORKDIR /api
#ENV TZ=America/sao_paulo

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

#CMD ["echo", "$MODEL_ID"]
#Downloading pre-trained model from google drive
RUN mkdir -p ./assets
    #&& gdown --id $MODEL_ID -O assets/best_model_state.bin

CMD ["bin/start_server"]

#sudo docker build -t sentiment-analysis-api .
#sudo docker run -e MODEL_ID=1-2Lnf3e1wN25WwhX35tMOqQM_8Ds-2Ey sentiment-analysis-api:latest