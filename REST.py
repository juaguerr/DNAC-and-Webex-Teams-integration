
import requests 
import json
from credentials import *
requests.packages.urllib3.disable_warnings()

class dnac_rest:
        
    def __init__(self, DNAC_IP, username, password):
        self.token = {}
        self.headers = {}
        self.get_token(DNAC_IP, username, password)
        self.DNAC_IP = DNAC_IP
                               
    def get_token(self, DNAC_IP, username, password):
        token_url = f"https://{DNAC_IP}:443/api/system/v1/auth/token"
        dnac_session = requests.post(url=token_url, auth=requests.auth.HTTPBasicAuth(username, password), verify=False)
        self.token = dnac_session.json()['Token']
        self.headers = {
        "Content-Type": "application/json",
        "x-auth-token": self.token
        }

    def get_request(self, api_url):
        url = f"https://{self.DNAC_IP}:443{api_url}"
        response = requests.get(url=url, headers= self.headers, verify=False)
        data = json.loads(response.content)
        return data
     
    def post_request(self, api_url, payload):
        url = f"https://{self.DNAC_IP}:443{api_url}"        
        dnac_session = requests.post(url=url, data = payload , headers = self.headers, verify=False)
        return dnac_session.content
    
    def put_request(self, api_url, payload):
        url = f"https://{self.DNAC_IP}:443{api_url}"        
        dnac_session = requests.put(url=url, data = payload , headers = self.headers, verify=False)
        return dnac_session.content
        
    def delete_request(self, api_url):
        url = f"https://{self.DNAC_IP}:443{api_url}"        
        dnac_session = requests.delete(url=url, headers= self.headers, verify=False)
        return dnac_session.content
    
dnac = dnac_rest(dDNAC_IP, dusername, dpassword)
