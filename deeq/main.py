import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.autograd import Function
from torchvision import datasets, transforms
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F
import qiskit
from qiskit.visualizatioin import *

class QuantumCircuit:
    """
    The class implements a simple Quantum Block
    """
    
    def __init__(self, num_qubits, backend, copies: int = 1000):
        self._circuit = qiskit.QuantumCircuit(num_qubits)
        self.theta = qiskit.circuit.Parameter('theta')
        self._circuit_.h([i for i in range(num_qubits)])
        
        
        pass
