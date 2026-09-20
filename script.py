                                        #Server Guard & Log Aggregator
import os
import json
import time
import requests

folder_name = 'server_logs'
file_name = 'status_report.json'
final_path = os.path.join(folder_name, file_name)

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print('Create folder: ''folder_name'' wait...  ')
    time.sleep(1.5)
    print('\nFolder "folder_name" is created')
print("Step 1 finished!")

server_url = 'https://httpbin.org/get'
response = requests.get(server_url)
server_data = response.json()
final_text = json.dumps(server_data, indent=4)
print(final_text)
try:
    serv1 = requests.get(server_url)
    serv2 = serv1.json()
    report_data = {
        'status': 'active',
        'server_response': serv2['url'],
        'check_time': time.time()
    }
    serv3 = json.dumps(report_data, indent=4)
except requests.exceptions.RequestException:
    report_data = {
        'status': 'down',
        'server_response': 'no_connection',
        'check_time': time.time()
    }
    serv3 = json.dumps(report_data, indent=4)
print(serv3)
with open(final_path, 'w', encoding='utf-8') as f:
    json.dump(report_data, f, indent=4)






