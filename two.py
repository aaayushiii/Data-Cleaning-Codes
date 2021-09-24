import pandas as pd
read_file = pd.read_csv ("./file1.txt")
read_file.to_csv ("./nndat.csv", index=None)
