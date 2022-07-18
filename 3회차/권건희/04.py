import json
from pprint import pprint
with open('data/movie.json', 'r',encoding='utf-8') as f:

    json_data = json.load(f)
    list=['id', 'title','vote_average', 'overview', 'genre_ids']
    dic_={}
    def movie_info(movie):
        for i in list:
            dic_[i]=movie[i]


        return dic_

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)
    
    pprint(movie_info(movie))