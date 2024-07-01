from ._anvil_designer import DependencyTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Dependency(DependencyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Populate grid panel
    dependency = anvil.server.call('get_dependency')
    self.repeating_panel_1.items = dependency
    
    # Populate dropdown 
    
    # Any code you write here will run before the form opens.

  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    rowPerPage = int(self.text_box_1.text) + 1
    if rowPerPage > 50:
      rowPerPage = 50
      
    self.data_grid_1.rows_per_page = rowPerPage

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    dependency_value = self.text_box_2.text
    dependency_description = self.text_box_3.text
    resource = self.drop_down_1.selected_value
    
    anvil.server.call('add_dependency',
                      dependency_value = dependency_value,
                      dependency_description = dependency_description,
                      resource = resource
                     )
    # Refresh the data in table
    anvil.server.call("get_dependency")
    
    # clear after adding new row
    self.text_box_1.text = ''
    self.text_box_2.text = ''
    self.drop_down_1.selected_value = self.drop_down_1.items[0]
