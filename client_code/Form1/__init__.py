from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def clear_input(self):
    self.Name_box.text = ""
    self.Email_box.text = ""
    self.Feed_backBox.text = ""
  
  def Submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.Name_box.text
    email = self.Email_box.text
    feedback = self.Feed_backBox.text

    anvil.server.call('send_feedback', name, email, feedback)
    Notification("Thanks for submitting").show()

    self.clear_inputs()



