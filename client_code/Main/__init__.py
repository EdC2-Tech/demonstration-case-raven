from ._anvil_designer import MainTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

from .Page1 import Page1
from .Page2 import Page2

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.link1.tag.form_to_open = Page1()
    self.link2.tag.form_to_open = Page2()
    # Any code you write here will run before the form opens.

  def link1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Page1')

  def link2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Page2')





