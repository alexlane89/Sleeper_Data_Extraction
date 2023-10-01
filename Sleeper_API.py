import requests
import json
from pandas.io.json._normalize import json_normalize
import pandas as pd

api_base = r'https://api.sleeper.app/v1/'
username = r'user/alexlane89'

def base_req(resolution):
    r=requests.get(api_base+resolution)
    json_info=r.json()
    return json_info

#r=requests.get(api_base+username)
#user_id = r.json()["user_id"]
#print(json.dumps(r.json(),indent=4))
#new = base_req(resolution=username)
user_id = base_req(resolution=username)["user_id"]
user_info = base_req(resolution=username)
#print(user_id)
year = 2020
s1=(r'user/'+user_id+r'/leagues/nfl/'+str(year))
league_20 = base_req(resolution=s1)
lid_20 = league_20[0]['league_id']
wk1 = base_req(resolution = (r'/league/' + lid_20 + r'/matchups/1'))
#l_s = pd.Series({year:lid_20})
draft_20=requests.get(api_base+r'/draft/'+league_20[0]['draft_id']+r'/picks')
d_20=draft_20.json()
d_ex=json_normalize(d_20)
d_ex.to_excel("sleeper.xlsx", sheet_name="draft picks")
