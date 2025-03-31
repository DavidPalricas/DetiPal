from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action

class ActionGreet(Action):
    """Action to greet the user (with or without their name)."""

    def name(self):
        """Name of the action."""
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Greet the user with their name (if provided)."""
        return []

class ActionSetName(Action):
    """Action to set the user's name."""

    def name(self):
        """Name of the action."""
        return "action_set_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Set the user's name and acknowledge it (if provided)."""
        return []
    
class ActionShowName(Action):
    """Action to show the user's name (if provided)."""
    
    def name(self):
        """Name of the action."""
        return "action_show_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Show the user's name (if provided)."""
        return []
