import torch
import torch.nn as nn
import numpy as np

class Simple(nn.Module):

    def __init__(self, num_classes=7):
        super(Simple, self).__init__()
        self.embedding = nn.Embedding(1000, 32)
        self.lstm = nn.LSTM(32, 32, 1) # try 200*32 if doesn't work
        self.dense1 = nn.Linear(32, 16)
        self.dense2 = nn.Linear(16, num_classes)


    def forward(self, x):
        x = self.embedding(x)
        x, _ = self.lstm(x)
        x = self.dense1(x)
        x = nn.functional.relu(x)
        x = self.dense2(x)
        return nn.functional.softmax(x, dim=2)

class RNN_LSTM(nn.Module):

    def __init__(self, num_classes=7):
        super(RNN_LSTM, self).__init__()
        self.embedding = nn.Embedding(1000, 32)


    def forward(self, x):
        return x
