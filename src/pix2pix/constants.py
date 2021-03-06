import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
LEARNING_RATE = 2e-4
BATCH_SIZE = 1
NUM_WORKERS = 4
L1_LAMBDA = 100
NUM_EPOCHS = 200
