from ._anvil_designer import RowTemplate4Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..GetResource import  resources as RES

class RowTemplate4(RowTemplate4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
      
    self.drop_down_1.items = RES
    # Any code you write here will run before the form opens.

  def edit_dependency(self):
    dependency_value = self.text_box_1.text
    dependency_description = self.text_box_2.text
    resource = self.drop_down_1.selected_value
    
    anvil.server.call('edit_dependency',
                      dependency_value = dependency_value,
                      dependency_description = dependency_description,
                      resource = resource)
    
  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.edit_dependency()

  def text_box_2_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.edit_dependency()

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    self.edit_dependency()

  

  
