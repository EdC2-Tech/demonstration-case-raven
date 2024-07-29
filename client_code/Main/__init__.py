from ._anvil_designer import MainTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

from ..Home import Home
from ..ViewData import ViewData
from ..Dependency import Dependency
from ..Resource import Resource
from ..UplinkTest import UplinkTest
from ..Gantt_Test import Gantt_Test
from ..Gantt_JS import Gantt_JS

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.content_panel.clear()
    self.content_panel.add_component(Home())
    # Any code you write here will run before the form opens.

  def home_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Home())

  def viewSch_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(ViewData())

  def resource_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Resource())

  def dependency_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Dependency())

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(UplinkTest())

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Gantt_Test())

  def outlined_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(Gantt_JS())

  


    

  







