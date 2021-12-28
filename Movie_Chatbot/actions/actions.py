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
    "host": "https://mv.i.tgcloud.io",
    "password": "Graph2367",
    "graphname": "MyGraph",
    "secret" : "adlr48p4mfj4r7oruor7tujt4j0q9s6e"
    }

################# TigerGraph Initialization ######################""
conn = tg.TigerGraphConnection(host=configs['host'], password=configs['password'], gsqlVersion="3.0.5", useCert=True, graphname=configs['graphname'])
conn.apiToken = conn.getToken(configs['secret'])
conn.gsql("USE graph {}".format(configs['graphname']))
#######################################"

class ActionMovieRec(Action):

    def name(self) -> Text:
        return "action_movie_recos"   # !!!! this return value must match line 55 of domain.yml  [ Step 4.a ]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print(tracker.latest_message)
        prediction = tracker.latest_message['entities'][0]['value']
        if prediction:
            query_response = conn.runInstalledQuery("RecommendMovies",{"p": prediction})
            recommendations = query_response[0]
            movies = recommendations["RecommendedMovies"]
            dispatcher.utter_message("Here are the top recommendations for user id:")
            dispatcher.utter_message(prediction)
            dispatcher.utter_message("*********************************************")
            for i in range(len(movies)):
                dispatcher.utter_message(movies[i]["attributes"]["title"])
                dispatcher.utter_message(movies[i]["attributes"]["genres"])
                dispatcher.utter_message("========================")

        return []


class ActionSearchPatientLocation(Action):

    def name(self) -> Text:
        return "action_patient_location"   # !!!! this return value must match line 56 of domain.yml  [ Step 4.a ]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(tracker.latest_message)
        prediction = tracker.latest_message['entities'][0]['value']

        ###### TigerGraph Query #####################    
        places = ""
        print(prediction)
        if prediction:
            places = conn.gsql("select state from Patient where patient_id == {} ".format(prediction))[0]["attributes"]['state']

        if len(places) > 0:
            dispatcher.utter_message(template="utter_infection_place_filled",place=places,userid=prediction)
        else:
            dispatcher.utter_message(template="utter_infection_place_empty")

        return []

class ActionInvestorExit(Action):

    def name(self) -> Text:
        return "action_investor_exit"   # !!!! this return value must match line 55 of domain.yml  [ Step 4.a ]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print(tracker.latest_message)
        prediction = tracker.latest_message['entities'][0]['value']
        print("======================")
        print(prediction)
        print("======================")
        if prediction:
            query_response = conn.runInstalledQuery("InvestorSuccessfulExits",{"p": prediction})
            print(query_response)
            vals = query_response[0]["results"]
            value = ",".join(vals)
        
        counts = len(vals)
        if counts > 0:
            dispatcher.utter_message(template="utter_movie_recos_filled",count=counts,userid=value)
        else:
            dispatcher.utter_message(template="utter_movie_recos_empty")

        return []

