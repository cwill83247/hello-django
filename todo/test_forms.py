from django.test import TestCase
from .forms import ItemForm

# Create your tests here.

class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})                        # simulating leaving the name field blank
        self.assertFalse(form.is_valid())                       # not sure ???
        self.assertIn('name', form.errors.keys())               # not sure ??
        self.assertEqual(form.errors['name'][0], 'This field is required.')  #extra check to see if this error message is showing 

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test toDo Item'})        # simulating putting an entry in name but leaving done field blank              
        self.assertTrue(form.is_valid())                       # not sure ???   
        

    def test_fields_are_onlyones_definedin_forms_py(self):
        form = ItemForm()        # starting a form             
        self.assertEqual(form.Meta.fields,['name', 'done'])    
            
