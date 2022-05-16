from app import app
from unittest import TestCase

class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""
        app.config['TESTING'] = True

    ###############################################################
    #testing create warehouse and list warehouses
    def test_warehouse_form(self):
        with app.test_client() as client:
            resp = client.get("/create-warehouse")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<button>create warehouse</button>', html)

    def test_create_warehouse(self):
        with app.test_client() as client:
            resp = client.post("/create-warehouse", data={'warehouse': 'warehouse B'})

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/items")

    def test_create_warehouse_error(self):
        with app.test_client() as client:
            resp = client.post("/create-warehouse", data={'warehouse': 'warehouse B'})
            

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/create-warehouse")

    def test_warehouse_list(self):
        with app.test_client() as client:
            resp = client.get('/warehouses')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<td>warehouse B</td>', html)

    ###############################################################
    #testing create and list items
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
    
    def test_create_item_error(self):
        with app.test_client() as client:
            resp = client.post('/items',
                           data={'id': 'adsfadsfasd',
                                 'name': 'cookie',
                                 'description': 'yummy cookies'})
            html = resp.get_data(as_text=True)

            
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, '/')
            

    def test_create_item(self):
        with app.test_client() as client:
            resp = client.post('/items',
                           data={'id': '4',
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

    ###############################################################
    #testing item details and item edit
    def test_item_details(self):
        with app.test_client() as client:
            resp = client.get("/item/4")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>cookie</h1>', html)

    def test_edit_item_error(self):
        with app.test_client() as client:
            resp = client.post('/item/4/edit',
                           data={'id': '',
                                 'name': 'cookie',
                                 'description': 'yummy cookies'})
            html = resp.get_data(as_text=True)

            
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/item/4/edit")
        
    def test_edit_item(self):
        with app.test_client() as client:
            resp = client.post("/item/4/edit", data={'id': '4',
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
            
    ###############################################################
    #testing assign routes
    def test_assign_form(self):
        with app.test_client() as client:
            resp = client.post("/items", data={'id': '5',
                                 'name': 'chocolate',
                                 'description': 'new description'})
            resp = client.get("/item/5/assign")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<button>assign item</button>', html)

    def test_assign_item(self):
        with app.test_client() as client:
            resp = client.post("/create-warehouse", data={'warehouse': 'warehouse A'})
            resp = client.post("/item/5/assign", data={'warehouse': 'warehouse A'})
            
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, '/item/5')

    def test_assign_item_error(self):
        with app.test_client() as client:
            resp = client.post("/item/5/assign", data={})
            
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/item/5/assign")

    ###############################################################
    #testing warehouse inventory route
    def test_warehouse_inventory(self):
        with app.test_client() as client:
            resp = client.get("/warehouse/1")
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>warehouse A Inventory</h1>', html)
    



