from ._anvil_designer import ResourceTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Resource(ResourceTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
      
    self.repeating_panel_1.items = app_tables.resource.search()
    # Any code you write here will run before the form opens.

  '''
  def addResource_button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    resourceName_textBox = TextBox(placeholder="Resource name")
    resourceDesc_textBox = TextBox(placeholder="Resource description")

    alert(content={resourceName_textBox, resourceDesc_textBox},
          title="Enter New Resource Details")
    app_tables.resource.add_row(resource_value=resourceName_textBox.text, resource_description=resourceDesc_textBox.text)
  '''
  
  def __update_table__(self):
    pass
    
