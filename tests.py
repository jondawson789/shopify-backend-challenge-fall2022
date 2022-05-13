from app import app
from unittest import TestCase

class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""
        app.config['TESTING'] = True

    def test_base_route(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<button>create item</button>', html)

    def test_items_route(self):
        with app.test_client() as client:
            resp = client.get('/items')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>List of Items</h1>', html)

    def test_create_item(self):
        with app.test_client() as client:
            resp = client.post('/items',
                           data={'id': '1',
                                 'name': 'cookie',
                                 'description': 'yummy cookies'})
            
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/items")


    def test_redirection_create_item(self):
        with app.test_client() as client:
            resp = client.get("/items", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<td>cookie</td>', html)

    def test_item_details(self):
        with app.test_client() as client:
            resp = client.get("/item/1")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>cookie</h1>', html)

    def test_edit_item(self):
        with app.test_client() as client:
            resp = client.post("/item/1/edit", data={'id': '1',
                                 'name': 'cookie',
                                 'description': 'new description'})

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/items")

    def test_redirection_edit_item(self):
        with app.test_client() as client:
            resp = client.get("/items", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<td>new description</td>', html)
            
    def test_create_warehouse(self):
        with app.test_client() as client:
            resp = client.post("/item/warehouse", data={'name': 'warehouse A'})

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/items")

    
    


