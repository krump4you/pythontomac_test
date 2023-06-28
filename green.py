import json
from whatsapp_api_client_python import API
#from config1 import idInstance, apiTokenInstance
from config1 import*
greenAPI = API.GreenApi(idInstance, apiTokenInstance)


def checkWA(phone_number):
    try:
        response = greenAPI.serviceMethods.checkWhatsapp(phone_number)
        if response.data["existsWhatsapp"] == True:
            return True
        else:
            return False
    except (KeyError, TypeError):
        return "skip"
