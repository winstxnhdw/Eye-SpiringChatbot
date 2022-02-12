import json
import numpy as np
import torch
import torch.nn as nn

from torch.utils.data import Dataset, DataLoader
from nltk_utils import *

from model import NeuralNet

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words =[]
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

# Stem and lowercase each word
ignore_words = [',', '.', '!', '?']
all_words = [stem(w) for w in all_words if w not in ignore_words]

# Remove duplicates and sort
all_words = sorted(set(all_words))
tags = sorted(set(tags))


# Create Training Data
X_train = []
Y_train = []
for (pattern_sentence, tag) in xy:
    bagwords = bag_of_words(pattern_sentence, all_words)
    X_train.append(bagwords)

    label = tags.index(tag)
    Y_train.append(label)


X_train = np.array(X_train)
Y_train = np.array(Y_train)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = Y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples


# CONSTANTS
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(X_train[0])
learning_rate = 0.001
num_epochs = 1000

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Loss and Optimizer
criterion = nn.CrossEntropyLoss()
optimzer = torch.optim.Adam(model.parameters(), lr = learning_rate)

# Training model
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)

        # Forward
        outputs = model(words)
        loss = criterion(outputs, labels)

        # Backward and optimizer Step
        optimzer.zero_grad()
        loss.backward()
        optimzer.step()

    if (epoch + 1) % 100 == 0:
        print(f'epoch {epoch+1}/{num_epochs}, loss = {loss.item():.4f}')


print(f'epoch {epoch+1}/{num_epochs}, loss = {loss.item():.4f}')

data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size": hidden_size,
    "all_words": all_words,
    "tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)

print(f'training complete! File saved to {FILE}')