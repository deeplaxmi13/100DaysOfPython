'''
{
    Key1 : [List],
    Key2 : {Dictionary}
}
'''

capitals = {
    "France":"Paris",
    "Germany":"Berlin"
}

travel_log={
    
    "France" : {
        "cities_visited": ["Paris","Lille","Dijon"],
        "total_visits":12
    },
    "Germany": {
        "cities_visited" : ["Berlin", "Hamburg","Stuttgart"],
        "total_visits" : 5
    },
}



#nesting a dictionary in a list

travel_log1=[
    {
        "country" : "France",
        "cities_visited": ["Paris","Lille","Dijon"],
        "total_visits":12
    },
    {
        "country" : "Germany",
        "cities_visited" : ["Berlin", "Hamburg","Stuttgart"],
        "total_visits" : 5
    },
]