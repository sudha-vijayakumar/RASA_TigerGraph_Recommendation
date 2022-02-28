# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pyTigerGraph as tg

################# TigerGraph Credentials ######################""
configs = {
    "host": "https://language.i.tgcloud.io/",
    "username": "tigergraph",
    "password": "tigergraph",
    "graphname": "WordNet",
    "secret" : "51gbt2nau9vbjh4m47njh0mmnpnrs6g7"
    }

################# TigerGraph Initialization ######################""
conn = tg.TigerGraphConnection(host=configs['host'], username = configs['username'], password=configs['password'], useCert=True, graphname=configs['graphname'])
conn.apiToken = conn.getToken(configs['secret'])
conn.gsql("USE graph {}".format(configs['graphname']))
#######################################"

print("Connected")

class ActionWordDef(Action):

    def name(self) -> Text:
        return "action_word_definition"   # !!!! this return value must match line 55 of domain.yml  [ Step 4.a ]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        prediction = tracker.latest_message['entities'][0]['value']
        
        if prediction:
            query_response = conn.runInstalledQuery("get_definition",{"word_to_query": prediction})
            response = query_response[0]
            # print(response)
            words = response["related_definition"]
            dispatcher.utter_message("Here is the list of definitions:")
            dispatcher.utter_message(words[0])
            dispatcher.utter_message("========================")

        return []

class ActionHypernym(Action):

    def name(self) -> Text:
        return "action_hypernym"   # !!!! this return value must match line 55 of domain.yml  [ Step 4.a ]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print(tracker.latest_message)
        prediction = tracker.latest_message['entities'][0]['value']

        if prediction:
            query_response = conn.runInstalledQuery("get_synonyms",{"word_to_query": prediction})
            response = query_response[0]
            # print(response)
            words = response["definition"]
            dispatcher.utter_message("Here is the list of hypernyms:")
            dispatcher.utter_message(words[0])
            dispatcher.utter_message("========================")

        return []

class ActionHyponym(Action):

    def name(self) -> Text:
        return "action_hyponym"   # !!!! this return value must match line 55 of domain.yml  [ Step 4.a ]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print(tracker.latest_message)
        prediction = tracker.latest_message['entities'][0]['value']

        if prediction:
            query_response = conn.runInstalledQuery("get_related_words",{"word_to_query": prediction})
            response = query_response[0]
            # print(response)
            words = response["definition"]
            dispatcher.utter_message("Here is the list of hyponyms:")
            dispatcher.utter_message(words[0])
            dispatcher.utter_message("========================")

        return []

class ActionAntonyms(Action):

    def name(self) -> Text:
        return "action_antonyms"   # !!!! this return value must match line 55 of domain.yml  [ Step 4.a ]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print(tracker.latest_message)
        prediction = tracker.latest_message['entities'][0]['value']

        if prediction:
            query_response = conn.runInstalledQuery("get_antonyms",{"word_to_query": prediction})
            response = query_response[0]
            # print(response)
            words = response["definition"]
            dispatcher.utter_message("Here is the list of antonyms:")
            dispatcher.utter_message(words[0])
            dispatcher.utter_message("========================")

        return []

class ActionAllConnections(Action):

    def name(self) -> Text:
        return "action_all_connections"   # !!!! this return value must match line 55 of domain.yml  [ Step 4.a ]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print(tracker.latest_message)
        prediction = tracker.latest_message['entities'][0]['value']

        if prediction:
            query_response = conn.runInstalledQuery("get_all_connections",{"word_to_query": prediction})
            response = query_response[0]
            # print(response)
            words = response["definition"]
            dispatcher.utter_message("Here is the list of related words:")
            dispatcher.utter_message(words[0])
            dispatcher.utter_message("========================")

        return []
