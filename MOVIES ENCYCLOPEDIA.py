import imdb,sys,time
from threading import Thread
def style(x,y,previous_length=0):
    #where x is the sring and y is fastness to print
    '''and it will return a length of string in previous
    length so that it can print len(x) number of 
    spaces to write it down properly'''

    sys.stdout.write("\r")
    sys.stdout.write(" "*previous_length)
    sys.stdout.flush()
    sys.stdout.write("\r")
    for a in x:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(y)
    return len(x)
def progress_bar(x):

    for i in range(100+1):
        time.sleep(x)
        sys.stdout.write(('.'*i)+(''*(100-i))+("\r [ %d"%i+"% ] "))
        sys.stdout.flush()
k=imdb.IMDb()
#MOVIES NAME SECTION
def movie_detail():
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
  
    style(f"Movie Name (year) : {Title}  ---> Released In : {Year}]\n",0.03,139)
    style(f"Rating : {Rating}\n",0.03)
    style(f"Movie Director Is||Are : {list_director}\n",0.02)
    style(f"Cast : {cast_list}\n",0.01)
#ACTOR NAME SECTION
def actor_detail():
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
    style(f"Name : {Name}\n",0.04,139)
    style(f"Date of birth : {DOB}\n",0.03)
    style(f"Height : {Height}\n",0.03)
    style(f"Trivia : {trivia[0]}\n",0.03)
    style(f'Movie apperences : {apper_list}\n',0.02)
#TOP/BOTTOM TEN MOVIES LIST SECTION
def top_list():
    top = k.get_top250_movies()                          #STORING THE TOP 250 MOVIES
    top1 = k.get_top250_tv()                             #STORING THE TOP 250 TV SERIES
    bottom = k.get_bottom100_movies()                    #STORING THE BOTTOM 100 MOVIES
    #PRINTING OUT THE RESULT USING FOR LOOP
    style("-----------------------:TOP 10 MOVIES:-----------------------\n",0.009,139)
    for i in top[0:10]:
        print(i)
    style("-----------------------:TOP 10 TV SERIES:-----------------------\n",0.009)
    for i in top1[0:10]:
        print(i)
    style("-----------------------:BOTTOM 10 MOVIES:-----------------------\n",0.009)
    for i in bottom[0:10]:
        print(i)

style('''WHY HAVE YOU REACHED OUT TO ME: \n1.INFO ON MOVIE STAR\n2.INFO ON MOIVE\n3.TOP 10 LIKE/DISLIKED MOVIES\n\n''',0.04)
previous_length=style("CHOOSE FAST - 1 || 2 || 3 : ",0.03)
c = input()
if c=='2':
    previous_length=style("Enter the name of the movie here : ",0.03,previous_length)
    m=input()
    print()         #TAKING INPUT FOR MOIVE
    Thread(target=movie_detail).start()
    style("processing... please wait --->",0.03)
    time.sleep(1)
    progress_bar(0.05) 
elif c=='1':
    style("Who are you searching for,try me! I may be quite helpful? : ",0.04)
    p=input()
    print()                                              #TAKING INPUT FOR PERSON TO BE SEARCHED
    Thread(target=actor_detail).start()
    style("processing... please wait --->",0.03)
    time.sleep(1)
    progress_bar(0.05)


elif c=='3':
    Thread(target=top_list).start()
    style("processing... please wait --->",0.03)
    time.sleep(0.3)
    progress_bar(0.06)
    print()
else:
    style("PLEASE DON'T WASTE MY TIME,CAN'T YOU READ THAT YOU HAVE TO CHOSE FROM ABOVE MENTIONED",0.01)

