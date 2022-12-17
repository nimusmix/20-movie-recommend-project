import requests
import json
import api_keys  # 숨겨놓은 api키

def get_movies(movie_id, page_num):
    api_key = api_keys.API_KEY
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/reviews?api_key={api_key}&language=ko&page={page_num}'
    print(url)
    response = requests.get(url).json()  # 받아오기
    results = response.get('results') 

    reviews = []
    for result in results:
        try:
            reviews.append(result["content"])
        except:
            pass
    
    print(len(reviews), '    ', response["id"])
    return reviews[:]


with open('final_youtube_1.json', 'r', encoding="UTF-8") as json_file:
    data_json_list = json.load(json_file)

result = []
for data_json in data_json_list:
    new_dict = {
        'id': data_json["pk"],
        "title": data_json["fields"]["title"],
        'reviews':get_movies(data_json["pk"], 1)
    }
    result.append(new_dict)
result.append(new_dict)


file_path = "./final_reviews_0.json"
with open(file_path, 'w', encoding="UTF-8") as outfile:
    json.dump(result, outfile, indent=4, ensure_ascii=False)
print(result)