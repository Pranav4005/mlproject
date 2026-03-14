import pathlib
p = pathlib.Path('templates/index.html')
raw = p.read_bytes()
print('len', len(raw))
print(raw)
print(raw.decode('utf-8', errors='replace'))
