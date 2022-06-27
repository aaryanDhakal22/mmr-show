import requests
import ast
from win10toast import ToastNotifier
from pprint import 


def js_to_py(text):
    text = text.replace('null','None')
    text = text.replace('false','False')
    text = text.replace('true','True')
    return text
# ------WRITE NAME INSIDE QUOTES------
name = 'Aaryeb'

r = requests.get("https://euw.whatismymmr.com/api/v1/summoner?name="+str(name)+"&v=6904765763")

results = js_to_py(r.text)
results_dict= ast.literal_eval(results)
ranked_mmr = results_dict['ranked']['avg']
normal_mmr = results_dict['normal']['avg']

toaster = ToastNotifier()
toaster.show_toast("MMR Update",
                   str("Ranked  :  "+str(ranked_mmr)+'\n'+'Normal  :  '+str(normal_mmr)),
                   icon_path="lol.ico",
                   duration=5)
  R YEN