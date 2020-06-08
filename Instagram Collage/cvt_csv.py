import insta
import pandas as pd

zer = insta.zero.reshape(184900, 3)
df = pd.DataFrame(zer, columns=['R', 'G', 'B'])
df.to_csv('abc.csv', index=False)
