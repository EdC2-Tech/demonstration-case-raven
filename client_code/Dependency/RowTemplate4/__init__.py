from ._anvil_designer import RowTemplate4Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..ResourceState import resources_available

class RowTemplate4(RowTemplate4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.res_dropdown.items = resources_available 


  def edit_dependency(self):
    dependency_value       = self.dep_val.text
    dependency_description = self.dep_des.text
    res                    = self.res_dropdown.selected_value
    
    anvil.server.call('edit_dependency',
                      self.item,
                      dependency_value = dependency_value,
                      dependency_description = dependency_description,
                      resource = res)
    
  def dep_val_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.edit_dependency()

  def dep_des_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.edit_dependency()

  def text_box_3_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.edit_dependency()
    
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    self.edit_dependency()



  

  
