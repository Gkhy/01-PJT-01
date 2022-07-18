import json
from pprint import pprint
with open('권건희/data/movie.json','r',encoding='utf-8') as f:
     file= open('권건희/data/genres.json','r',encoding='utf-8')
     fdata= json.load(f)
     filedata=json.load(file)
     list=('id','title','vote_average','overview')
     dic_={}
     genre_names=[]
     def movie_info(movie, genres):
        ids=movie['genre_ids']
        for key in list:
            dic_[key]=movie[key]
        for i in range(17):
            if genres[i]['id'] in ids:
                genre_names.append(genres[i]['name'])
        dic_['genre_names']=genre_names
        return dic_

        
         
    # 여기에 코드를 작성합니다.id, title, vote_average, overview, genre_names  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('권건희/data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('권건희/data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))