import pandas as pd
from compute_pnl import compute_pnl

data = pd.DataFrame([
    ['AAPL', 'Buy', 10, 100.0, 1000.0],
    ['AAPL', 'Sell', 10, 110.0, 1100.0]
], columns=['Instrument', 'Type', 'Quantity', 'Price', 'Amount'])

print(compute_pnl(data))
