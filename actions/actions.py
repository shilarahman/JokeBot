# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import secrets


#googletranslate API
import googletrans
class ActionGoogleTranslate(Action): 
    from googletrans import Translator


     def name(self) -> Text:
        return "action_googletranslate" 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            Text = next(tracker.get_latest_entity_values("googletransl"),
                               None) 

            translator = Translator()
            dispatcher.utter_message(text="Bonjour! I think you speak" +(translator.detect(Text))+ text="I can translate what you just said to English:"+(translator.translate(Text)))
            dispatcher.utter_message(text="Sorry i am still learning and will soon respond to you in your desired language")
            dispatcher.utter_message(response="utter_default")
            
            return []

class ActionTellJoke(Action):

    def name(self) -> Text:
        return "action_tell_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        jokeCat = ["good", "bad", "ok"]

        # Tell a random joke and ask for feedback
        dispatcher.utter_message(response="utter_" + secrets.choice(jokeCat) + "_joke")
        dispatcher.utter_message(response="utter_ask_for_feedback")

        return []

class ActionHandleFeedback(Action):

    def name(self) -> Text:
        return "action_handle_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recentSentiment = next(tracker.get_latest_entity_values("sentiment"),
                               None)  # Extracts the most recent sentiment
        if recentSentiment == "pos":
            dispatcher.utter_message(response="utter_feedback_good")  # Utter good feedback response, only if feedback
            # is good
        elif recentSentiment is None:
            dispatcher.utter_message(response="utter_default")  # Handle case where there is no intent/sentiment
            # extracted
        else:
            dispatcher.utter_message(response="utter_feedback_bad")  # If feedback is neutral or negative utter bad
            # feedback

        return []

#wikipedia API
import wikipedia
class ActionWikipedia(Action):

    def name(self) -> Text:
        return "action_wiki"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            Search = next(tracker.get_latest_entity_values("wikisearch"),
                               None)  
    
            ##shows relevant information
        
            print(wikipedia.page(wikipedia.search(Search).content)
            
        or:
            dispatcher.utter_message(text = "Sorry, this search is unavailable right now please try another")

        return []


