import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arry = np.array(list).reshape(3, 3)
    
    calculations = {
        'mean': [
            arry.mean(axis=0).tolist(),
            arry.mean(axis=1).tolist(),
            arry.mean().item()
        ],
        'variance': [
            arry.var(axis=0).tolist(),
            arry.var(axis=1).tolist(),
            arry.var().item()
        ],
        'standard deviation': [
            arry.std(axis=0).tolist(),
            arry.std(axis=1).tolist(),
            arry.std().item()
        ],
        'max': [
            arry.max(axis=0).tolist(),
            arry.max(axis=1).tolist(),
            arry.max().item()
        ],
        'min': [
            arry.min(axis=0).tolist(),
            arry.min(axis=1).tolist(),
            arry.min().item()
        ],
        'sum': [
            arry.sum(axis=0).tolist(),
            arry.sum(axis=1).tolist(),
            arry.sum().item()
        ]
    }
    
    return calculations