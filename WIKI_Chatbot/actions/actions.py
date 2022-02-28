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

# Connection parameters
hostName = "https://language.i.tgcloud.io/"
userName = "tigergraph"
password = "tigergraph"

conn = tg.TigerGraphConnection(host=hostName, username=userName, password=password)
print("Connected")

conn.graphname="WordNet"
secret = conn.createSecret()
authToken = conn.getToken(secret)
authToken = authToken[0]
conn = tg.TigerGraphConnection(host=hostName, graphname="WordNet", username=userName, password=password, apiToken=authToken)


################# TigerGraph Initialization ######################""

conn.gsql("USE graph WordNet")
#######################################"

class ActionWordDef(Action):

    def name(self) -> Text:
        return "action_word_definition"   # !!!! this return value must match line 55 of domain.yml  [ Step 4.a ]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print(tracker.latest_message)
        prediction = tracker.latest_message['entities'][0]['value']

        if prediction:
            query_response = conn.runInstalledQuery("get_definition",{"word_to_query": prediction})
            response = query_response[0]
            # print(response)
            words = response["word_definition"]
            dispatcher.utter_message("Here is word definition:")
            dispatcher.utter_message(words[0])
            dispatcher.utter_message("========================")

        return []

class ActionRelatedWords(Action):

    def name(self) -> Text:
        return "action_related_words"   # !!!! this return value must match line 55 of domain.yml  [ Step 4.a ]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print(tracker.latest_message)
        prediction = tracker.latest_message['entities'][0]['value']

        if prediction:
            query_response = conn.runInstalledQuery("get_related_words",{"word_to_query": prediction})
            response = query_response[0]
            # print(response)
            words = response["related_words"]
            dispatcher.utter_message("Here is the list of related words:")
            dispatcher.utter_message(words[0])
            dispatcher.utter_message("========================")

        return []

class ActionWordPos(Action):

    def name(self) -> Text:
        return "action_word_pos"   # !!!! this return value must match line 55 of domain.yml  [ Step 4.a ]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print(tracker.latest_message)
        prediction = tracker.latest_message['entities'][0]['value']

        if prediction:
            query_response = conn.runInstalledQuery("get_pos",{"word_to_query": prediction})
            response = query_response[0]
            # print(response)
            words = response["related_pos"]
            dispatcher.utter_message("Here is the list of POS:")
            dispatcher.utter_message(words[0])
            dispatcher.utter_message("========================")

        return []
