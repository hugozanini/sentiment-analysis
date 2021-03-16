FROM python:3.8-slim-buster
WORKDIR /api
#ENV TZ=America/sao_paulo

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 8000
RUN mkdir -p ./assets
CMD ["bin/start_server"]

#sudo docker build -t sentiment-analysis-api .
#sudo docker run -e MODEL_ID=1-2Lnf3e1wN25WwhX35tMOqQM_8Ds-2Ey -p 8000:8000 sentiment-analysis-api:latest