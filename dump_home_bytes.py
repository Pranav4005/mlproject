import pathlib
p = pathlib.Path('templates/home.html')
raw = p.read_bytes()
print('len', len(raw))
print(raw[:500])
