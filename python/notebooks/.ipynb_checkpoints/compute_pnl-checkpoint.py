def compute_pnl(df):
    stats = {}
    for _, row in df.iterrows():
        key = row['Instrument']
        qty, amt, price, typ = row['Quantity'], row['Amount'], row['Price'], row['Type']
        if key not in stats:
            stats[key] = {'qty': 0.0, 'cost': 0.0, 'pnl': 0.0}
        s = stats[key]
        if typ == 'Buy':
            s['qty'] += qty
            s['cost'] += amt
        elif typ == 'Sell':
            avg_cost = s['cost'] / s['qty'] if s['qty'] else 0
            realized = (price - avg_cost) * qty
            s['pnl'] += realized
            s['qty'] -= qty
            s['cost'] -= avg_cost * qty
    return {k: v['pnl'] for k, v in stats.items()}
