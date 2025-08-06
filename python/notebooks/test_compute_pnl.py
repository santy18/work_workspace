import pandas as pd
from compute_pnl import compute_pnl

def test_pnl():
    data = pd.DataFrame([
        ['AAPL', 'Buy', 10, 100.0, 1000.0],
        ['AAPL', 'Sell', 10, 110.0, 1100.0]
    ], columns=['Instrument', 'Type', 'Quantity', 'Price', 'Amount'])
    result = compute_pnl(data)
    assert 'AAPL' in result and abs(result['AAPL'] - 100.0) < 1e-6
