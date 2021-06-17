from tqdm import tqdm
from time import sleep
from random import random


def evaluate():
    result = random() 
    if result < 0.2:
        return "no_change"
    if result < 0.8:
        return "ok"
    if result < 0.95:
        return "warning"
    return "error"


with tqdm(total=100) as pbar:
    for i in range(100):
        sleep(0.1)
        result = evaluate()
        pbar.update(1, label=result)
print(pbar.type_count)
