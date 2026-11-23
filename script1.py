from logging.handlers import RotatingFileHandler
import json
import logging
import requests
import os
import time
import sys
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
os.makedirs(config.get('logs_dir', 'ai_datasets'), exist_ok=True)
log_formatted = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = RotatingFileHandler(
    'ai_datasets/downloader.log',
    maxBytes=1024 * 1024 * 5,
    backupCount=3,
    encoding='utf-8',
)
file_handler.setFormatter(log_formatted)

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatted)

my_logger = logging.getLogger('Text')
my_logger.setLevel(logging.INFO)
my_logger.addHandler(file_handler)
my_logger.addHandler(console_handler)

def check_server(target_url: str) -> None:
    try:
        time_start = time.time()
        my_logger.info(f'Sending request to {target_url}')
        server_request = requests.get(target_url, timeout=config.get('timeout_sec', 10))
        server_request.raise_for_status()
        data = server_request.json()
        status = data.get('model_status', 'Unknown')
        temp = data.get('gpu_temp', 0)
        my_logger.info(f'Done! Server returned code: {server_request.status_code}. Time elapsed: {round(time.time() - time_start, 2)} sec.')
        my_logger.info(f"Parsed metrics -> Status: {status} | GPU Temp: {temp}C")
    except requests.exceptions.RequestException as err:
        my_logger.critical(f'SERVER IS CRUSHED!\nInside details: {err}')
    except Exception as unexpected_err:
        my_logger.error(f'Unexpected error: {unexpected_err}')
    finally:
        my_logger.info('Script execution cycle finished.')
if __name__ == '__main__':
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = config.get('default_url', 'http://127.0.0.1:8000')
    check_server(target)

