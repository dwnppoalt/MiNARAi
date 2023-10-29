import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
class Wolfram:
    def __init__(self):
        self.appid = "UHU78Q-9E8A5RWA82"
        self.simpleURL = "http://api.wolframalpha.com/v1/simple?"
        self.shortAnswersURL = "http://api.wolframalpha.com/v1/result?"
        self.FRnSbSURL = "http://api.wolframalpha.com/v2/query?"
    
    def simple(self, query: str) -> str:
        params = {"appid" : self.appid, "i" : query}
        url = self.simpleURL + urlencode(params)
        return url
    
    def shortAnswers(self, query: str) -> dict:
        params = {'appid' : self.appid, 'i' : query}
        url = self.shortAnswersURL + urlencode(params)
        r = requests.get(url)
        return r.text
    
    def fullResults(self, query):
        param = {"appid" : self.appid, "input" : query, "podstate" : "Result__Step-by-step solution","output" : "json"}
        obj = requests.get(self.FRnSbSURL + urlencode(param)).json().get('queryresult')
        if obj.get('pods') == None:
            try:
                items = {"didyoumeans" : [obj.get("didyoumeans").get("val")]}
            except:
                items = {"didyoumeans" : [i.get('val') for i in obj.get("didyoumeans")]}
        else:
            items =  {
                    "pods" : [
                        {
                            "dataType" : pod.get("title"),
                            "subpods" : [
                                {
                                    'data' : subpod.get("plaintext"),
                                    'alt' : subpod.get("img").get("alt"),
                                    'img' : subpod.get("img").get("src"),

                                } for subpod in pod.get("subpods")
                            ]
                        } for pod in obj.get("pods")

                    ],
                    "didyoumeans" : [i for i in obj.get("didyoumeans")] if obj.get("didyoumeans") else [],
                }
        return items

