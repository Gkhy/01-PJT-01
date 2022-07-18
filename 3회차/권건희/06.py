import json
from pprint import pprint
with open('권건희/data/movies.json','r',encoding='utf-8')as f:
     file= open('권건희/data/genres.json','r',encoding='utf-8')
     fdata=json.load(f)
     filedata=json.load(file)



     def movie_info(movies, genres):
        genres_names=[]
        all=[]
        for movie in movies:
            for genre in genres :

                if genre["id"]in movie["genre_ids"]:
                    genres_names.append(genre["name"])   
            all.append({'genres_names':genres_names,'id':movie["id"],'overview':movie["overview"],'title':movie["title"],'vote_average':movie["vote_average"]})
            genres_names=[]  
        return all    
        

     if __name__ == '__main__':
        movies_json = open('권건희/data/movies.json', encoding='UTF8')
        movies_list = json.load(movies_json)

        genres_json = open('권건희/data/genres.json', encoding='UTF8')
        genres_list = json.load(genres_json)

        pprint(movie_info(movies_list, genres_list))