import requests

class Grammar:
    def __init__(self) -> None:
        self.URL = "https://gdemo-pukjs.ondigitalocean.app/check"
        self.headers = {
            'referer' : 'https://gdemo-pukjs.ondigitalocean.app/',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69'
            }
    
    def grammar(self, text):
        data = {
            'txt' : text,
            'language' : 'en'
        }
        r = requests.post(url=self.URL, data=data, headers=self.headers)
        return r.text
    


class Paraphrase:
    def __init__(self):
        self.URL = "https://www.paraphraser.io/frontend/rewriteArticleBeta"
        self.headers = {
            'referer' : 'https://www.paraphraser.io/',
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69"
            }
        self.cookie = "ci_session=a%3A6%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22cc3bb7fb7801db6ec7e2a98ffff70f0f%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A9%3A%22127.0.0.1%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F118.0.0.0+Safari%2F537.36+Edg%2F118.%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1698568996%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22authcheck%22%3Bs%3A20%3A%22paraphrase1698568996%22%3B%7Dc0d1a485378c1f956c627c6d03929e97; _gid=GA1.2.1807418093.1698568998; _ga_Q3XGSV1HE8=GS1.1.1698568997.1.1.1698569034.0.0.0; _ga_WGYTCZ2REQ=GS1.1.1698568998.1.1.1698569035.0.0.0; _ga=GA1.2.1889798235.1698568998"

        