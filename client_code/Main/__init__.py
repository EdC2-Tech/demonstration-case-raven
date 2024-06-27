from ._anvil_designer import MainTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.

  def home_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.refresh_data_bindings()

  def viewSch_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main.ViewData')

  def resource_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main.Resource')

  def dependency_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Main.Dependency')


    

  







