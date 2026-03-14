from app import app

with app.test_client() as c:
    rv = c.get('/')
    print('status', rv.status_code)
    print('len', len(rv.data))
    print(rv.data[:200])
