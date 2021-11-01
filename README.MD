## Deploy BERT for Sentiment Analysis in Portuguese

This repo is part of the tutorial on how to transfer learning a BERT model to perform sentiment analysis in Portuguese. 

The tutorial is divided into two parts. In the first one, you're going to learn how to scrap data from the google play store to create a dataset in Portuguese.
In the second post, you're going to see how to use FastAPI, Uvicorn, and Docker to deploy the trained model as a REST API and achieve results as shown below:


<img src="https://raw.githubusercontent.com/hugozanini/sentiment-analysis/main/media/bert_example.gif" width="500">


The project is based on microservices and all the architecture is built as code using docker compose and bash scripts.

<img src="https://raw.githubusercontent.com/hugozanini/sentiment-analysis/main/media/flow_data.png" width="600">


### Referências
[0] Vaswani, Ashish, et al. “Attention is all you need.” _arXiv preprint arXiv:1706.03762_ (2017).

[1] Devlin, Jacob, et al. “Bert: Pre-training of deep bidirectional transformers for language understanding.” _arXiv preprint arXiv:1810.04805_ (2018).

[2] Vaswani, Ashish, et al. “Atte_nti_on is all you need.” _arXiv preprint arXiv:1706.03762_ (2017).

[3] Devlin, Jacob, et al. “Bert: Pre-training of deep bidirectional transformers for language understanding.” _arXiv preprint arXiv:1810.04805_ (2018).

[4] Valkov, Venelin. “Bert for Sentiment Analysis using Pytorch, Transformers by Hugging Face and FASTAPI.” March 1, 2020.

[5] “FastAPI Documentation .” FASTAPI. Accessed November 1, 2021. [https://fastapi.tiangolo.com/.](https://fastapi.tiangolo.com/.)
