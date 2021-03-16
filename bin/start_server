#!/bin/bash

#Downloading pre-trained model
if [ ! -d assets/best_model_stated.bin ]; then
  gdown --id $MODEL_ID -O assets/best_model_state.bin
fi

#Going to the sentiment_analyser/api.py and referencing to the app
uvicorn sentiment_analyzer.api:app --host 0.0.0.0