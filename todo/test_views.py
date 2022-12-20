from django.test import TestCase
from .models import Item                          # need this for the edit item test 

# Create your tests here.

class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')                             #load the home page
        self.assertEqual(response.status_code, 200)                 # check we get a 200 status message 
        self.assertTemplateUsed(response, 'todo/todo_list.html')    # check template being used 


    def test_get_additem_page(self):
        response = self.client.get('/add')                             #load the home page
        self.assertEqual(response.status_code, 200)                 # check we get a 200 status message 
        self.assertTemplateUsed(response, 'todo/add_item.html')    # check template being used 


    def test_get_edititem_page(self):
        item = Item.objects.create(name='Using test to create an item')
        response = self.client.get(f'/edit/{item.id}')                             #using an f string to pass int he item id of the item created above 
        self.assertEqual(response.status_code, 200)                 # check we get a 200 status message 
        self.assertTemplateUsed(response, 'todo/edit_item.html')    # check template being used 
    
    
    def test_can_additem(self):
        response =self.client.post('/add',{'name': 'adding a test entry'})
        self.assertRedirects(response, '/')                                      # checkign after entry addded redirects to home page

    def test_can_deleteitem(self):
        item = Item.objects.create(name='Using test to create an item')
        response = self.client.get(f'/delete/{item.id}')                             #using an f string to pass int he item id of the item created above 
        self.assertRedirects(response, '/') 
        existing_items = Item.objects.filter(id=item.id)                # creates a variable to add items however ti shoudl be blank as deleted item above  
        self.assertEqual(len(existing_items),0)
    

    def test_can_toggleitem(self):
        item = Item.objects.create(name='Using test to create an item', done=True)
        response = self.client.get(f'/toggle/{item.id}')                             #using an f string to pass int he item id of the item created above 
        self.assertRedirects(response, '/') 
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)



            
