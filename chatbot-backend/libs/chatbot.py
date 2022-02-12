import random
import json
import torch

from libs.model import NeuralNet
from libs.nltk_utils import *

class ChatBot:

    def __init__(self):

        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        with open('data/intents.json', 'r') as f:
            self.intents = json.load(f)

        data = torch.load("model/data.pth")
        input_size = data["input_size"]
        hidden_size = data["hidden_size"]
        output_size = data["output_size"]
        model_state = data["model_state"]
        self.all_words = data["all_words"]
        self.tags = data["tags"]

        self.model = NeuralNet(input_size, hidden_size, output_size).to(device)
        self.model.load_state_dict(model_state)
        self.model.eval()

    def reply(self, text):

        sentence = tokenize(text)
        X = bag_of_words(sentence, self.all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X)

        output = self.model(X)
        _, predicted = torch.max(output, dim = 1)
        tag = self.tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.75:
            for intent in self.intents["intents"]:
                if tag == intent["tag"]:
                    return random.choice(intent['responses'])
        else:
            return "I do not understand..."