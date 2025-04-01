# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv

class ActionCourseInfo(Action):
    def name(self) -> Text:
        return "action_course_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the most recent user message
        latest_message = tracker.latest_message
        
        # Extract entities from the latest message
        entities = latest_message.get('entities', [])
        
        # Look for course-related entities in the current message
        course_info = None
        entity_type = None
        
        for entity in entities:
            if entity['entity'] in ['curso', 'codigo', 'sigla_curso']:
                course_info = entity['value']
                entity_type = entity['entity']
                break
        
        # If no entity in current message, check if we have any in slots
        if not course_info:
            # Check slots in order of preference
            if tracker.get_slot("curso"):
                course_info = tracker.get_slot("curso")
                entity_type = "curso"
            elif tracker.get_slot("sigla_curso"):
                course_info = tracker.get_slot("sigla_curso")
                entity_type = "sigla_curso"
            elif tracker.get_slot("codigo"):
                course_info = tracker.get_slot("codigo")
                entity_type = "codigo"
        
        if course_info:
            # entity_type_display = entity_type.replace("course_", "") if entity_type else "information"
            dispatcher.utter_message(text=f"I see you're interested in the {course_info} course.")
            
            with open("deti_resourses/curso_cod.csv", 'r', encoding='utf-8') as file:
                # skip the first line (header)
                next(file)
                csv_reader = csv.reader(file)
                found = False
                
                # Find the course in the CSV file based on the entity type
                for row in csv_reader:
                    match = False
                    
                    if entity_type == "codigo" and course_info.lower() == row[0].lower():
                        match = True
                    elif entity_type == "curso" and course_info.lower() in row[1].lower():
                        match = True
                    elif entity_type == "sigla_curso" and course_info.lower() == row[2].lower():
                        match = True
                    
                    if match:
                        found = True
                        dispatcher.utter_message(text="Here are some details about it:")
                        dispatcher.utter_message(text=f"Course name: {row[1]}")
                        dispatcher.utter_message(text=f"Course code: {row[0]}")
                        dispatcher.utter_message(text=f"Course acronym: {row[2]}")
                        dispatcher.utter_message(text=f"Course's degree: {row[3]}")
                        return []
                
                if not found:
                    dispatcher.utter_message(text="Unfortunately I do not have any information about that course.")
                    return []
        else:
            dispatcher.utter_message(text="I understand you're asking about a course, but I couldn't identify which one.")
            dispatcher.utter_message(text="Try specifying the course by its name, code, or acronym.")

        return []

class ActionDisciplinaInfo(Action):
    def name(self) -> Text:
        return "action_disciplina_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the most recent user message
        latest_message = tracker.latest_message
        
        # Extract entities from the latest message
        entities = latest_message.get('entities', [])
        
        # Look for course-related entities in the current message
        course_info = None
        entity_type = None
        
        for entity in entities:
            if entity['entity'] in ['disciplina', 'codigo', 'sigla_disciplina']:
                course_info = entity['value']
                entity_type = entity['entity']
                break
        
        # If no entity in current message, check if we have any in slots
        if not course_info:
            # Check slots in order of preference
            if tracker.get_slot("sigla_disciplina"):
                course_info = tracker.get_slot("sigla_disciplina")
                entity_type = "sigla_disciplina"
            elif tracker.get_slot("disciplina"):
                course_info = tracker.get_slot("disciplina")
                entity_type = "disciplina"
            elif tracker.get_slot("codigo"):
                course_info = tracker.get_slot("codigo")
                entity_type = "codigo"
        
        if course_info:
            # entity_type_display = entity_type.replace("course_", "") if entity_type else "information"
            dispatcher.utter_message(text=f"I see you're interested in the {course_info} course.")
            
            with open("deti_resourses/curso_cod.csv", 'r', encoding='utf-8') as file:
                # skip the first line (header)
                next(file)
                csv_reader = csv.reader(file)
                found = False
                
                # Find the course in the CSV file based on the entity type
                for row in csv_reader:
                    match = False
                    
                    if entity_type == "codigo" and course_info.lower() == row[0].lower():
                        match = True
                    elif entity_type == "curso" and course_info.lower() in row[1].lower():
                        match = True
                    elif entity_type == "sigla_curso" and course_info.lower() == row[2].lower():
                        match = True
                    
                    if match:
                        found = True
                        dispatcher.utter_message(text="Here are some details about it:")
                        dispatcher.utter_message(text=f"Course name: {row[1]}")
                        dispatcher.utter_message(text=f"Course code: {row[0]}")
                        dispatcher.utter_message(text=f"Course acronym: {row[2]}")
                        dispatcher.utter_message(text=f"Course's degree: {row[3]}")
                        return []
                
                if not found:
                    dispatcher.utter_message(text="Unfortunately I do not have any information about that course.")
                    return []
        else:
            dispatcher.utter_message(text="I understand you're asking about a course, but I couldn't identify which one.")
            dispatcher.utter_message(text="Try specifying the course by its name, code, or acronym.")

        return []