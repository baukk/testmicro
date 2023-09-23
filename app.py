from flask import Flask, request, jsonify
import requests
import json
import time

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    all_the_urls = request.args.getlist('url')
    all_numbers_list = []  

    for url in all_the_urls:
        try:
            start_time = time.time()
            res = requests.get(url, timeout=0.5) # timeout is 0.5 seconds. We're unable to retrieve all three lists bc of the timeout limit
            if res.status_code == 200:
                data = res.json()
                numbers = data.get('numbers', [])
                all_numbers_list.extend(numbers)
                print(f"checking {url}: {numbers}")  
            elif res.status_code == 408:     # 408 is timeout
                continue
        except Exception as e:
            print(f"Error  {url}: {str(e)}")  
            continue

    merged_numbers = sorted(list(set(all_numbers_list)))  # set because we want unique numbers only
    return jsonify({"numbers": merged_numbers})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
