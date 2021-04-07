#MOVIES DESCRIPTION,MOVIES STAR SEARCH AND TOP TEN MOST LIKE/DISLIKED LIST USING IMDB MODULE
import imdb
k=imdb.IMDb()
print('''WHY HAVE YOU REACHED OUT TO ME: \n1.INFO ON MOVIE STAR\n2.INFO ON MOIVE\n3.TOP 10 LIKE/DISLIKED MOVIES''')
c = input('CHOOSE FAST(1/2/3): ')
if c=='2':
    m=input("ENTER THE MOVIE NAME: ")                   #TAKING INPUT FOR MOIVE
    movies = k.search_movie(str(m))                     #SEARCHING FOR ALL MOIVES RELATED TO THE NAME ENTERED
    index = movies[0].getID()                           #TAKING THE [0] INDEX MOVIE OUT OF THE LIST
    movie = k.get_movie(index)
    Title = movie['title']                              #STORING THE TITLE
    Year = movie['year']                                #STORING THE YEAR OF RELEASE
    Rating = movie['rating']                            #STORING THE RATING
    Cast = movie['cast']                                #STORING THE CAST
    cast_list = ', '.join(map(str,Cast))                #CONVERTING TO THE LIST JOINED WITH ","
    Di = movie['director']
    list_director = ' '.join(map(str,Di))
    #PRINTING OUT THE RESULTS
    print(f"Movie name(year):{Title}------{Year}")
    print(f"Rating: {Rating}")
    print(f'Movie director is/are:',list_director)
    print(f"Cast:{cast_list}")
elif c=='1':
    p=input("ENTER THE ONE YOU ARE SEARCHING FOR: ")     #TAKING INPUT FOR PERSON TO BE SEARCHED
    star = k.search_person(str(p))                       ##SEARCHING FOR ALL PERSON RELATED TO THE NAME ENTERED
    index = star[0].getID()                              #TAKING THE [0] INDEX PERSON OUT OF THE LIST
    st = k.get_person(index)
    bio = k.get_person_biography(index)                  #STORING THE BIOGRAPHY ACCORDING TO INDEX WE GOT
    Name = st['name']                                    #STORING THE NAME
    DOB = st['birth date']                               #STORING THE DATE OF BIRTH
    Height = st['height']                                #STORING THE HEIGHT
    trivia = st['trivia']                                #STORING THE TRIVIA
    apperences = bio['titlesRefs']                       #STORING THE TITLE REFRENCES
    apper_list = ', '.join(map(str, apperences))         #CONVERTING TO THE LIST JOINED WITH ","
    #PRINTING OUT THE RESULTS
    print(f"Name:{Name}")
    print(f"Date of birth: {DOB}")
    print(f"Height:{Height}")
    print(f"Trivia:{trivia[0]}")
    print(f'Movie apperences:{apper_list}')
elif c=='3':
    top = k.get_top250_movies()                          #STORING THE TOP 250 MOVIES
    top1 = k.get_top250_tv()                             #STORING THE TOP 250 TV SERIES
    bottom = k.get_bottom100_movies()                    #STORING THE BOTTOM 100 MOVIES
    #PRINTING OUT THE RESULT USING FOR LOOP
    print("-----------------------:TOP 10 MOVIES:-----------------------")
    for i in top[0:10]:
        print(i)
    print("-----------------------:TOP 10 TV SERIES:-----------------------")
    for i in top1[0:10]:
        print(i)
    print("-----------------------:BOTTOM 10 MOVIES:-----------------------")
    for i in bottom[0:10]:
        print(i)
    print()
else:
    print("PLEASE DON'T WASTE MY TIME,CAN'T YOU READ THAT YOU HAVE TO CHOSE FROM ABOVE MENTIONED")


