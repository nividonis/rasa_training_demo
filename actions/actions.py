# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from datetime import datetime
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.utils.request_weather import *
from actions.utils.request_corona_cases import *
from actions.utils.send_email import *

class ActionGetWeather(Action):

    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = "Darmstadt"

        result = get_weather(city)

        weather = result["weather"]
        temp = result["temp"]
        feels_like = result["feels_like"]
        temp_min = result["temp_min"]
        temp_max = result["temp_max"]

        dispatcher.utter_message("Today in {}:\nThe weather is {}.\nThe temperature is currently {} degree Celsius and feels like {} degree Celsius\nThe daytime high temperature and the low temperature are {}, {} degrees Celsius, respectively.".format(city, weather, temp,feels_like, temp_max, temp_min))

        return []


class ActionGetCoronaCases(Action):

    def name(self) -> Text:
        return "action_get_corona_cases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        country = tracker.get_slot("country")

        if country is None:
            country = "Germany"

        cases_num = get_corona_cases(country)


        dispatcher.utter_message(template="utter_corona_cases",
                                 total_cases=cases_num[0],
                                 deaths=cases_num[1],
                                 recovered=cases_num[2])
        return []

class ActionSendEmails(Action):

    def name(self) -> Text:
        return "action_send_emails"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email = tracker.get_slot("email")

        send_emails(email)

        return []


class ActionSayHi(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        now =  datetime.now()

        if now.hour >= 0 and now.hour <= 12:
            msg = "Good morning"
        elif now.hour >= 12 and now.hour <=16:
            msg = "Good day"
        else:
            msg = "Good evening"

        dispatcher.utter_message(msg)

        return []

