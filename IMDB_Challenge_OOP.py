from selenium import webdriver
from time import sleep
import pandas as pd

# def web_extraction():
#     movie_names = []
#     release_date = []
#     description = []
#     directors = []
#     movie_stars = []
#     ratings = []
#     duration = []
#     genre = []

#     url = 'https://www.imdb.com/list/ls009668711/?sort=moviemeter,asc&st_dt=&mode=detail&page=1;
#     pth = 'chromedriver.exe'

#     driver = webdriver.Chrome(pth)

#     driver.get(url)
    
#     sleep(20)

#     movies = 100
#     for i in range(1,movies+1):
        
#         movie = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/h3/a')
                                    
#         release = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/h3/span[2]')

                                                 
#         desc = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[2]')
                                                
#         dire = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[3]/a[1]')

#         rat = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/div[1]/div[1]/span[2]')

#         dura = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[1]/span[3]')

#         gen = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[1]/span[5]')
                                            
#         movie_ = movie.text
#         movie_names.append(movie_)
        
#         whole = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[3]')
#         whole_ = whole.text
#         director, space, stars = whole_.partition('Stars: ')
#         movie_stars.append(stars)
    
    
#         release_ = release.text
#         find_wo_brackets = release_.replace('(','')
#         find_wo_brackets = find_wo_brackets.replace(')','')

#         if i == 10:
#             find_wo_brackets = 2004
#         if i == 38:
#             find_wo_brackets = 2015
#         if i == 84:
#             find_wo_brackets = 2006
#         release_date.append(int(find_wo_brackets))

#         description_ = desc.text
#         description.append(description_)

#         directors_ = dire.text
#         directors.append(directors_)

#         ratings_ = rat.text
#         int_ratings_ = float(ratings_)
#         ratings.append(int_ratings_)

#         duration_ = dura.text
#         durat, space, stri = duration_.partition(' ')
#         int_duration = int(durat)
#         duration.append(int_duration)

#         genres_ = gen.text
#         genre.append(genres_)

# #########################################       SAVING IT INTO PANDAS DATAFRAME        #######################################################################
  
#     data = {'Movies':movie_names,'Description':description,'Directors':directors,'Movie Stars':movie_stars,'Genre':genre,'Release Date':release_date,'Duration (in mins)':duration,'Ratings':ratings}
    
    
    
#     labels = pd.RangeIndex(start=1,stop=movies+1,step=1)
    
#     df = pd.DataFrame(data,index =labels).rename_axis('Serial Number',axis=1)
#     df.to_csv('drama_imdb.csv')
    
#     return df

# web_extraction()


class WebScrappingIMDB:

    def __init__(self,number_of_movies_extract):
        self.number_of_movies_to_extract = number_of_movies_extract

    def webextraction(self):
        movie_names = []
        release_date = []
        description = []
        directors = []
        movie_stars = []
        ratings = []
        duration = []
        genre = []

        url = 'https://www.imdb.com/list/ls009668711/?sort=moviemeter,asc&st_dt=&mode=detail&page=1';
        pth = 'chromedriver.exe'

        driver = webdriver.Chrome(pth)

        driver.get(url)
            
        sleep(20)

    
        for i in range(1,self.number_of_movies_to_extract+1,1):
                
            movie = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/h3/a')
                                            
            release = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/h3/span[2]')
                                
            desc = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[2]')
                                                        
            dire = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[3]/a[1]')

            rat = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/div[1]/div[1]/span[2]')

            dura = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[1]/span[3]')

            gen = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[1]/span[5]')
                                                    
            movie_ = movie.text
            movie_names.append(movie_)
                
            whole = driver.find_element_by_xpath(f'/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[3]/div[{i}]/div[2]/p[3]')
            whole_ = whole.text
            director, space, stars = whole_.partition('Stars: ')
            movie_stars.append(stars)
            
            release_ = release.text
            find_wo_brackets = release_.replace('(','')
            find_wo_brackets = find_wo_brackets.replace(')','')

            if i == 70:
                find_wo_brackets = 2015
            if i == 76:
                find_wo_brackets = 2004
            if i == 93:
                find_wo_brackets = 2006
                
            release_date.append(int(find_wo_brackets))

            description_ = desc.text
            description.append(description_)

            directors_ = dire.text
            directors.append(directors_)

            ratings_ = rat.text
            int_ratings_ = float(ratings_)
            ratings.append(int_ratings_)

            duration_ = dura.text
            durat, space, stri = duration_.partition(' ')
            int_duration = int(durat)
            duration.append(int_duration)

            genres_ = gen.text
            genre.append(genres_)

#########################################################################       SAVING IT INTO PANDAS DATAFRAME        ####################################################################################
        
        data = {'Movies':movie_names,'Description':description,'Directors':directors,'Movie Stars':movie_stars,'Genre':genre,'Release Date':release_date,'Duration (in mins)':duration,'Ratings':ratings}
            
        labels = pd.RangeIndex(start=1,stop=self.number_of_movies_to_extract+1,step=1)
            
        df = pd.DataFrame(data,index =labels).rename_axis('Serial Number',axis=1)
        df.to_csv('drama_imdb_viaOOP.csv')
            
        return df

extraction_from_IMDB = WebScrappingIMDB(100)

print(extraction_from_IMDB.webextraction())