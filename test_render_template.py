from app import app

with app.app_context():
    tmpl = app.jinja_env.get_or_select_template('index.html')
    print('template exists:', tmpl)
    rendered = tmpl.render()
    print('rendered len', len(rendered))
    print(rendered)