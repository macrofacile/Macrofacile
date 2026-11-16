for k, lst in P.items():
    for i, h in enumerate(lst, 1):
        open(f'{OUT}/{k}-{i}.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{h}</body></html>')
print('ok')
