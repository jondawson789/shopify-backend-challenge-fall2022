# shopify-backend-challenge-fall2022

This web app was built for shopify's fall 2022 backend intern challenge. It was built using flask (python) as the framework. 

The base route will render a create item form: the user can enter a unique integer id (required), item name (optional), and item description (optional), and hit create item to create the item. Entering a duplicate id, non integer id, or no id will throw an error and the user will return to the create item form to enter a valid id. A successful item creation will redirect the user to the items page which will list all the inventory items. 

The items page will list the id, name, and desription of each item. Clicking on the item details page will render a page listing the item's details: name, warehouse location, and description. There is also a delete button, edit button, and assign to warehouse button. The delete button will delete the item from the inventory list. The edit button will render an edit item form, and the user can edit any item details he/she wishes, however a valid and unique id must be entered. The assign warehouse button will render a dropdown list of all warehouses, and the user can select the warehouse to assign the item to, but a warehouse must exist for the form to be submitted.

Clicking on the create warehouse hyperlink will render a create warehouse form. The user can enter any unique string such as warehouse name or location to create a warehouse, but the user can't submit an empty string. After creating a warehouse, the user can view a list of all warehouses by clicking the warehouse list hyperlink. The user can click on the warehouse's inventory hyperlink to view a list of all the inventory assigned to that warehouse. There are also two other hyperlinks: a create item hyperlink to render the create item form, and a item list hyperlink to list all inventory items. 

The app is deployed on heroku: https://fall2022-inventory-app.herokuapp.com/items

