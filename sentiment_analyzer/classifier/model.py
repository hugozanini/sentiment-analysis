import json
import torch
import torch.nn.functional as F
from transformers import BertTokenizer

from .sentiment_classifier import SentimentClassifier

with open("config.json") as json_file:
    config = json.load(json_file)


class Model:
    def __init__(self):
        self.device = torch.device("cuda:0" if torch.cuda.is_available()
                                    else "cpu")
        self.tokenizer = BertTokenizer.from_pretrained(config["BERT_MODEL"])

        classifier = SentimentClassifier(len(config["CLASS_NAMES"]))
        classifier.load_state_dict(
            torch.load(config['PRE_TRAINED_MODEL'], map_location=self.device)
        )
        classifier = classifier.eval()
        self.classifier = classifier.to(self.device)

    def predict(self, text):
        encoded_text = \
            self.tokenizer.encode_plus( text,
                                        max_lenght = config["MAX_SEQUENCE_LEN"],
                                        add_special_tokens = True,
                                        return_token_type_ids = False,
                                        pad_to_max_length = True,
                                        return_attetion_mask = True,
                                        return_tensors = "pt")
        input_ids = encoded_text["input_ids"].to(self.device)
        attention_mask = encoded_text["attention_mask"].to(self.device)

        with torch.no_grad():
            #Getting the prediction
            probabilities = F.softmax(self.classifier(input_ids, attention_mask),
                            dim = 1)

        #Taking the most confident result
        confidence, predicted_class = torch.max(probabilities, dim = 1)
        predicted_class = predicted_class.cpu().item()
        probabilities = probabilities.flatten().cpu().numpy().tolist()

        return(
            config["CLASS_NAMES"][predicted_class],
            confidence,
            dict(zip(config["CLASS_NAMES"], probabilities))
        )

'''
As the model initialization is heavy, let's use the singleton pattern to
make it only once
'''

model = Model()
def get_model():
    return model