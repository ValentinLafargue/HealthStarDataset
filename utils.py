import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import math

class Network(nn.Module):
    def __init__(self, init_column, 
                 activation_bool = False,
                 last_batch_norm = False,
                 n_nodes = 512,
                 n_loop = 4,
                 ):
        
        super().__init__()
        self.activation_bool = activation_bool
        self.seq = nn.Sequential()
        self.seq.append(nn.BatchNorm1d(init_column))
        self.seq.append(nn.Linear(init_column, n_nodes))
        self.seq.append(nn.ReLU())

        for i in range(n_loop):
            self.seq.append(nn.BatchNorm1d(n_nodes))
            self.seq.append(nn.Linear(n_nodes, n_nodes))
            self.seq.append(nn.ReLU())
        
        if last_batch_norm:
            self.seq.append(nn.BatchNorm1d(n_nodes))
        self.seq.append(nn.Linear(n_nodes, 1))
        self.activation = nn.Sigmoid()

    def forward(self, x):
        prob = self.seq(x)
        if self.activation_bool:
            return self.activation(prob)
        return prob
    
class Network_dropout(nn.Module):
    def __init__(self, init_column, 
                 activation_bool = False,
                 n_nodes = 512,
                 n_loop = 4,
                 ):
        super().__init__()
        self.activation_bool = activation_bool
        self.seq = nn.Sequential()
        self.seq.append(nn.Linear(init_column, n_nodes))
        self.seq.append(nn.ReLU())

        for i in range(n_loop):
            self.seq.append(nn.Dropout(0.2))
            self.seq.append(nn.Linear(n_nodes, n_nodes))
            self.seq.append(nn.ReLU())

        self.seq.append(nn.Linear(n_nodes, 1))
        self.activation = nn.Sigmoid()

    def forward(self, x):
        prob = self.seq(x)
        if self.activation_bool:
            return self.activation(prob)
        return prob
    

def training_network_threshold(model,
                     optimizer,
                     X_train,
                     Y_train,
                     X_test,
                     Y_test,
                     epochs,
                     batch_size,
                     ):
    list_loss_train = np.zeros((epochs, math.ceil(len(X_train)//batch_size)))
    list_loss_test  = np.zeros((epochs, math.ceil(len(X_test)//batch_size)))

    for epoch in range(1,epochs+1):
        #Train
        model.train()
        optimizer.train()

        for batch_count in range(math.ceil(len(X_train)//batch_size)):
            optimizer.zero_grad()
            x,y = X_train[(batch_count*batch_size):((batch_count+1)*batch_size)].float(), (Y_train[(batch_count*batch_size):((batch_count+1)*batch_size)]).float()
            output = model(x)
            batch_loss = ((y - output.squeeze())**2).mean() #loss(y, output.squeeze())
            batch_loss.backward()
            optimizer.step()

            list_loss_train[epoch-1, batch_count] = batch_loss.item()

        with torch.no_grad():
            optimizer.eval()
            for batch_count in range(5):
                x = X_train[(batch_count*batch_size):((batch_count+1)*batch_size)].float()
                output = model(x)
        model.eval()

        #Test
        for batch_count in range(math.ceil(len(X_test)//batch_size)):
            x,y = X_test[(batch_count*batch_size):((batch_count+1)*batch_size)].float(), (Y_test[(batch_count*batch_size):((batch_count+1)*batch_size)]).float()
            output = model(x.float())
            batch_loss =  ((y - output.squeeze())**2).mean() #loss(y, output.squeeze())

            list_loss_test[epoch-1, batch_count] = batch_loss.item()
            
    return list_loss_train, list_loss_test