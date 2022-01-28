import pandas as pd
import matplotlib.pyplot as plt

data = {
    "test": [0,1,2,3,4,5],
    "results": ["a", "b", "c","d", "e"]
}

df = pd.DataFrame(data=data)
df.head
