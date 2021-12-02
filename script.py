import pandas as pd
import json
import requests
import time
import sys

# csv: <string> csv path
# url: <string> url to request
# time: <int> time in seconds between requests
def requesting(csv, url, seconds):
    df = pd.read_csv(csv, delimiter=';')
    
    # Converting rows to json records
    df['json'] = df.apply(lambda x: x.to_json(force_ascii=False), axis=1)
   
    # Assigning 'json' column values creating a panda.Series
    series = df['json']

    # Iterating over size of Series
    for row in range(len(series)):
        # Creating json dictionary
        json_content =  json.loads(series[row])
        
        # Formatting message 
        message = {"message": json_content}
        
        # Post requisition
        result = requests.post(url, json=message)
        
        # Showing request's result
        print("Test", row ," - Result: " , result.json())

        # Pausing for a few seconds
        time.sleep(seconds)
    # Leaving   
    print("Leaving...")
#

requesting(csv = sys.argv[1], url = sys.argv[2], seconds = int(sys.argv[3]))

# requesting(csv = 'produtos.csv', url = 'http://localhost:8000/predictor', seconds = 1)
# python script.py produtos.csv http://localhost:8000/predictor 1