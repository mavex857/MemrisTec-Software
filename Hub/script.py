import torch
import numpy as np


class myNetwork(torch.nn.Module):
    def __init__(self, in_features=10, out_features=1):
        super(myNetwork, self).__init__()
        self.linear = torch.nn.Linear(in_features, out_features)

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred


net = myNetwork()
print(net(torch.randn(1, 10)))
