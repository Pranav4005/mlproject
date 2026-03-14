content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ML Project</title>
</head>
<body>
  <h1>Welcome</h1>
  <p><a href="/predictdata">Go to prediction form</a></p>
</body>
</html>
'''

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
