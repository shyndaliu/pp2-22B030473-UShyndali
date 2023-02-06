movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def func1(x):
    for i in movies:
        if i["name"]==x:
            return i["imdb"]>5.5

#print(func1("We Two"))

def func2():
    a=[]
    for i in movies:
        if i["imdb"]>5.5:
            a.append(i["name"])
    return a


#print(func2())

def func3(category):
    a=[]
    for i in movies:
        if i["category"]==category:
            a.append(i["name"])
    return a

#print(func3("Thriller"))

def func4():
    x=0
    cnt=0;
    for i in movies:
        cnt+=1
        x+=i["imdb"]
    return x/cnt

#print(func4())

def func5(category):
    x=0
    cnt=0;
    for i in movies:
        if i["category"]==category:
            cnt+=1
            x+=i["imdb"]
    return x/cnt

#print(func5("Romance"))