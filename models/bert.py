'''
Author: Sylvain Dec 2022
'''

import torch
import torch.nn as nn
from transformers import BertModel


class Bert(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.bert = BertModel.from_pretrained('bert-base-uncased')
        self.linear = nn.Linear(768, 10)

    def forward(self,**inputs):
        x = self.bert(inputs['x'])
        outputs_prob = self.linear(x[0][:, 0, :])
        return outputs_prob

