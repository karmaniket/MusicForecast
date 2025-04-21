import pandas as pd
import numpy as np
import random
from datetime import datetime

np.random.seed(42)
random.seed(42)

real_songs = [
    # Pop Songs
    {"artist": "Taylor Swift", "title": "Blank Space", "year": 2014, "genre": "pop", "popularity": 92},
    {"artist": "Taylor Swift", "title": "Cruel Summer", "year": 2019, "genre": "pop", "popularity": 95},
    {"artist": "Taylor Swift", "title": "Anti-Hero", "year": 2022, "genre": "pop", "popularity": 94},
    {"artist": "Taylor Swift", "title": "Lover", "year": 2019, "genre": "pop", "popularity": 90},
    {"artist": "Taylor Swift", "title": "All Too Well", "year": 2012, "genre": "pop", "popularity": 89},
    {"artist": "Ed Sheeran", "title": "Shape of You", "year": 2017, "genre": "pop", "popularity": 98},
    {"artist": "Ed Sheeran", "title": "Perfect", "year": 2017, "genre": "pop", "popularity": 94},
    {"artist": "Ed Sheeran", "title": "Thinking Out Loud", "year": 2014, "genre": "pop", "popularity": 93},
    {"artist": "Ed Sheeran", "title": "Photograph", "year": 2014, "genre": "pop", "popularity": 89},
    {"artist": "Ariana Grande", "title": "thank u, next", "year": 2019, "genre": "pop", "popularity": 93},
    {"artist": "Ariana Grande", "title": "7 rings", "year": 2019, "genre": "pop", "popularity": 89},
    {"artist": "Ariana Grande", "title": "positions", "year": 2020, "genre": "pop", "popularity": 88},
    {"artist": "Justin Bieber", "title": "Sorry", "year": 2015, "genre": "pop", "popularity": 96},
    {"artist": "Justin Bieber", "title": "Stay", "year": 2021, "genre": "pop", "popularity": 95},
    {"artist": "Justin Bieber", "title": "Love Yourself", "year": 2015, "genre": "pop", "popularity": 91},
    {"artist": "Billie Eilish", "title": "bad guy", "year": 2019, "genre": "pop", "popularity": 97},
    {"artist": "Billie Eilish", "title": "Happier Than Ever", "year": 2021, "genre": "pop", "popularity": 88},
    {"artist": "Billie Eilish", "title": "everything i wanted", "year": 2019, "genre": "pop", "popularity": 86},
    {"artist": "The Weeknd", "title": "Blinding Lights", "year": 2020, "genre": "pop", "popularity": 100},
    {"artist": "The Weeknd", "title": "Save Your Tears", "year": 2020, "genre": "pop", "popularity": 92},
    {"artist": "The Weeknd", "title": "The Hills", "year": 2015, "genre": "pop", "popularity": 93},
    {"artist": "Dua Lipa", "title": "Don't Start Now", "year": 2019, "genre": "pop", "popularity": 94},
    {"artist": "Dua Lipa", "title": "Levitating", "year": 2020, "genre": "pop", "popularity": 95},
    {"artist": "Dua Lipa", "title": "New Rules", "year": 2017, "genre": "pop", "popularity": 91},
    {"artist": "Harry Styles", "title": "As It Was", "year": 2022, "genre": "pop", "popularity": 96},
    {"artist": "Harry Styles", "title": "Watermelon Sugar", "year": 2019, "genre": "pop", "popularity": 90},
    {"artist": "Harry Styles", "title": "Adore You", "year": 2019, "genre": "pop", "popularity": 88},
    {"artist": "Olivia Rodrigo", "title": "drivers license", "year": 2021, "genre": "pop", "popularity": 97},
    {"artist": "Olivia Rodrigo", "title": "good 4 u", "year": 2021, "genre": "pop", "popularity": 96},
    {"artist": "Olivia Rodrigo", "title": "vampire", "year": 2023, "genre": "pop", "popularity": 94},
    {"artist": "Adele", "title": "Hello", "year": 2015, "genre": "pop", "popularity": 93},
    {"artist": "Adele", "title": "Easy On Me", "year": 2021, "genre": "pop", "popularity": 91},
    {"artist": "Adele", "title": "Rolling in the Deep", "year": 2011, "genre": "pop", "popularity": 92},
    {"artist": "BTS", "title": "Dynamite", "year": 2020, "genre": "pop", "popularity": 93},
    {"artist": "BTS", "title": "Butter", "year": 2021, "genre": "pop", "popularity": 92},
    {"artist": "BTS", "title": "Boy With Luv", "year": 2019, "genre": "pop", "popularity": 90},
    {"artist": "Katy Perry", "title": "Roar", "year": 2013, "genre": "pop", "popularity": 89},
    {"artist": "Katy Perry", "title": "Dark Horse", "year": 2013, "genre": "pop", "popularity": 88},
    {"artist": "Lady Gaga", "title": "Shallow", "year": 2018, "genre": "pop", "popularity": 91},
    {"artist": "Lady Gaga", "title": "Bad Romance", "year": 2009, "genre": "pop", "popularity": 90},
    
    # Hip-Hop/Rap
    {"artist": "Drake", "title": "God's Plan", "year": 2018, "genre": "hip-hop", "popularity": 95},
    {"artist": "Drake", "title": "Hotline Bling", "year": 2015, "genre": "hip-hop", "popularity": 91},
    {"artist": "Drake", "title": "One Dance", "year": 2016, "genre": "hip-hop", "popularity": 93},
    {"artist": "Drake", "title": "In My Feelings", "year": 2018, "genre": "hip-hop", "popularity": 94},
    {"artist": "Kendrick Lamar", "title": "HUMBLE.", "year": 2017, "genre": "hip-hop", "popularity": 94},
    {"artist": "Kendrick Lamar", "title": "Alright", "year": 2015, "genre": "hip-hop", "popularity": 87},
    {"artist": "Kendrick Lamar", "title": "DNA.", "year": 2017, "genre": "hip-hop", "popularity": 92},
    {"artist": "Travis Scott", "title": "SICKO MODE", "year": 2018, "genre": "hip-hop", "popularity": 96},
    {"artist": "Travis Scott", "title": "goosebumps", "year": 2016, "genre": "hip-hop", "popularity": 90},
    {"artist": "Travis Scott", "title": "HIGHEST IN THE ROOM", "year": 2019, "genre": "hip-hop", "popularity": 89},
    {"artist": "Cardi B", "title": "WAP", "year": 2020, "genre": "hip-hop", "popularity": 97},
    {"artist": "Cardi B", "title": "Bodak Yellow", "year": 2017, "genre": "hip-hop", "popularity": 92},
    {"artist": "Cardi B", "title": "I Like It", "year": 2018, "genre": "hip-hop", "popularity": 93},
    {"artist": "Post Malone", "title": "Rockstar", "year": 2017, "genre": "hip-hop", "popularity": 94},
    {"artist": "Post Malone", "title": "Circles", "year": 2019, "genre": "hip-hop", "popularity": 93},
    {"artist": "Post Malone", "title": "Sunflower", "year": 2018, "genre": "hip-hop", "popularity": 95},
    {"artist": "Lil Nas X", "title": "Old Town Road", "year": 2019, "genre": "hip-hop", "popularity": 99},
    {"artist": "Lil Nas X", "title": "MONTERO", "year": 2021, "genre": "hip-hop", "popularity": 92},
    {"artist": "Lil Nas X", "title": "INDUSTRY BABY", "year": 2021, "genre": "hip-hop", "popularity": 94},
    {"artist": "Megan Thee Stallion", "title": "Savage", "year": 2020, "genre": "hip-hop", "popularity": 93},
    {"artist": "Megan Thee Stallion", "title": "Body", "year": 2020, "genre": "hip-hop", "popularity": 89},
    {"artist": "Kanye West", "title": "Stronger", "year": 2007, "genre": "hip-hop", "popularity": 88},
    {"artist": "Kanye West", "title": "Gold Digger", "year": 2005, "genre": "hip-hop", "popularity": 87},
    {"artist": "Eminem", "title": "Lose Yourself", "year": 2002, "genre": "hip-hop", "popularity": 91},
    {"artist": "Eminem", "title": "Without Me", "year": 2002, "genre": "hip-hop", "popularity": 90},
    {"artist": "Jay-Z", "title": "Empire State of Mind", "year": 2009, "genre": "hip-hop", "popularity": 89},
    {"artist": "Jay-Z", "title": "99 Problems", "year": 2003, "genre": "hip-hop", "popularity": 86},
    {"artist": "Nicki Minaj", "title": "Super Bass", "year": 2011, "genre": "hip-hop", "popularity": 89},
    {"artist": "Nicki Minaj", "title": "Anaconda", "year": 2014, "genre": "hip-hop", "popularity": 87},
    
    # Rock
    {"artist": "Imagine Dragons", "title": "Radioactive", "year": 2012, "genre": "rock", "popularity": 87},
    {"artist": "Imagine Dragons", "title": "Believer", "year": 2017, "genre": "rock", "popularity": 90},
    {"artist": "Imagine Dragons", "title": "Thunder", "year": 2017, "genre": "rock", "popularity": 89},
    {"artist": "Coldplay", "title": "Viva la Vida", "year": 2008, "genre": "rock", "popularity": 85},
    {"artist": "Coldplay", "title": "The Scientist", "year": 2002, "genre": "rock", "popularity": 83},
    {"artist": "Coldplay", "title": "Yellow", "year": 2000, "genre": "rock", "popularity": 84},
    {"artist": "Twenty One Pilots", "title": "Stressed Out", "year": 2015, "genre": "rock", "popularity": 89},
    {"artist": "Twenty One Pilots", "title": "Heathens", "year": 2016, "genre": "rock", "popularity": 87},
    {"artist": "Twenty One Pilots", "title": "Ride", "year": 2015, "genre": "rock", "popularity": 86},
    {"artist": "Foo Fighters", "title": "Everlong", "year": 1997, "genre": "rock", "popularity": 82},
    {"artist": "Foo Fighters", "title": "Learn to Fly", "year": 1999, "genre": "rock", "popularity": 78},
    {"artist": "Foo Fighters", "title": "The Pretender", "year": 2007, "genre": "rock", "popularity": 80},
    {"artist": "Arctic Monkeys", "title": "Do I Wanna Know?", "year": 2013, "genre": "rock", "popularity": 86},
    {"artist": "Arctic Monkeys", "title": "505", "year": 2007, "genre": "rock", "popularity": 84},
    {"artist": "Red Hot Chili Peppers", "title": "Californication", "year": 1999, "genre": "rock", "popularity": 84},
    {"artist": "Red Hot Chili Peppers", "title": "Under the Bridge", "year": 1991, "genre": "rock", "popularity": 83},
    {"artist": "Red Hot Chili Peppers", "title": "Snow (Hey Oh)", "year": 2006, "genre": "rock", "popularity": 82},
    {"artist": "Queen", "title": "Bohemian Rhapsody", "year": 1975, "genre": "rock", "popularity": 89},
    {"artist": "Queen", "title": "Don't Stop Me Now", "year": 1978, "genre": "rock", "popularity": 87},
    {"artist": "Linkin Park", "title": "In the End", "year": 2000, "genre": "rock", "popularity": 86},
    {"artist": "Linkin Park", "title": "Numb", "year": 2003, "genre": "rock", "popularity": 85},
    {"artist": "Nirvana", "title": "Smells Like Teen Spirit", "year": 1991, "genre": "rock", "popularity": 87},
    {"artist": "Nirvana", "title": "Come as You Are", "year": 1991, "genre": "rock", "popularity": 84},
    {"artist": "Green Day", "title": "Boulevard of Broken Dreams", "year": 2004, "genre": "rock", "popularity": 85},
    {"artist": "Green Day", "title": "American Idiot", "year": 2004, "genre": "rock", "popularity": 84},
    
    # R&B
    {"artist": "Beyoncé", "title": "Halo", "year": 2008, "genre": "r&b", "popularity": 89},
    {"artist": "Beyoncé", "title": "Formation", "year": 2016, "genre": "r&b", "popularity": 86},
    {"artist": "Beyoncé", "title": "Crazy in Love", "year": 2003, "genre": "r&b", "popularity": 88},
    {"artist": "Rihanna", "title": "Diamonds", "year": 2012, "genre": "r&b", "popularity": 92},
    {"artist": "Rihanna", "title": "Umbrella", "year": 2007, "genre": "r&b", "popularity": 90},
    {"artist": "Rihanna", "title": "Work", "year": 2016, "genre": "r&b", "popularity": 91},
    {"artist": "Frank Ocean", "title": "Thinkin Bout You", "year": 2012, "genre": "r&b", "popularity": 83},
    {"artist": "Frank Ocean", "title": "Novacane", "year": 2011, "genre": "r&b", "popularity": 80},
    {"artist": "The Weeknd", "title": "Starboy", "year": 2016, "genre": "r&b", "popularity": 91},
    {"artist": "The Weeknd", "title": "Can't Feel My Face", "year": 2015, "genre": "r&b", "popularity": 90},
    {"artist": "SZA", "title": "Good Days", "year": 2020, "genre": "r&b", "popularity": 87},
    {"artist": "SZA", "title": "Kill Bill", "year": 2022, "genre": "r&b", "popularity": 92},
    {"artist": "SZA", "title": "Love Galore", "year": 2017, "genre": "r&b", "popularity": 85},
    {"artist": "Alicia Keys", "title": "No One", "year": 2007, "genre": "r&b", "popularity": 85},
    {"artist": "Alicia Keys", "title": "Fallin'", "year": 2001, "genre": "r&b", "popularity": 84},
    {"artist": "Usher", "title": "Yeah!", "year": 2004, "genre": "r&b", "popularity": 88},
    {"artist": "Usher", "title": "Burn", "year": 2004, "genre": "r&b", "popularity": 85},
    {"artist": "Daniel Caesar", "title": "Best Part", "year": 2017, "genre": "r&b", "popularity": 86},
    {"artist": "Jhené Aiko", "title": "The Worst", "year": 2013, "genre": "r&b", "popularity": 83},
    
    # Electronic/Dance
    {"artist": "Calvin Harris", "title": "Summer", "year": 2014, "genre": "electronic", "popularity": 85},
    {"artist": "Calvin Harris", "title": "This Is What You Came For", "year": 2016, "genre": "electronic", "popularity": 88},
    {"artist": "Calvin Harris", "title": "One Kiss", "year": 2018, "genre": "electronic", "popularity": 87},
    {"artist": "Avicii", "title": "Wake Me Up", "year": 2013, "genre": "electronic", "popularity": 89},
    {"artist": "Avicii", "title": "Levels", "year": 2011, "genre": "electronic", "popularity": 87},
    {"artist": "Avicii", "title": "The Nights", "year": 2014, "genre": "electronic", "popularity": 85},
    {"artist": "Marshmello", "title": "Happier", "year": 2018, "genre": "electronic", "popularity": 86},
    {"artist": "Marshmello", "title": "Friends", "year": 2018, "genre": "electronic", "popularity": 84},
    {"artist": "Zedd", "title": "The Middle", "year": 2018, "genre": "electronic", "popularity": 87},
    {"artist": "Zedd", "title": "Clarity", "year": 2012, "genre": "electronic", "popularity": 84},
    {"artist": "Zedd", "title": "Stay", "year": 2017, "genre": "electronic", "popularity": 85},
    {"artist": "David Guetta", "title": "Titanium", "year": 2011, "genre": "electronic", "popularity": 86},
    {"artist": "David Guetta", "title": "Hey Mama", "year": 2015, "genre": "electronic", "popularity": 85},
    {"artist": "Daft Punk", "title": "Get Lucky", "year": 2013, "genre": "electronic", "popularity": 88},
    {"artist": "Daft Punk", "title": "Around the World", "year": 1997, "genre": "electronic", "popularity": 84},
    {"artist": "Skrillex", "title": "Bangarang", "year": 2011, "genre": "electronic", "popularity": 83},
    {"artist": "Skrillex", "title": "Scary Monsters and Nice Sprites", "year": 2010, "genre": "electronic", "popularity": 82},
    {"artist": "Swedish House Mafia", "title": "Don't You Worry Child", "year": 2012, "genre": "electronic", "popularity": 84},
    {"artist": "Martin Garrix", "title": "Animals", "year": 2013, "genre": "electronic", "popularity": 85},
    
    # Country
    {"artist": "Luke Combs", "title": "Beautiful Crazy", "year": 2018, "genre": "country", "popularity": 82},
    {"artist": "Luke Combs", "title": "Hurricane", "year": 2016, "genre": "country", "popularity": 80},
    {"artist": "Luke Combs", "title": "When It Rains It Pours", "year": 2017, "genre": "country", "popularity": 81},
    {"artist": "Morgan Wallen", "title": "Whiskey Glasses", "year": 2018, "genre": "country", "popularity": 83},
    {"artist": "Morgan Wallen", "title": "7 Summers", "year": 2020, "genre": "country", "popularity": 81},
    {"artist": "Morgan Wallen", "title": "Wasted on You", "year": 2021, "genre": "country", "popularity": 82},
    {"artist": "Chris Stapleton", "title": "Tennessee Whiskey", "year": 2015, "genre": "country", "popularity": 82},
    {"artist": "Chris Stapleton", "title": "Starting Over", "year": 2020, "genre": "country", "popularity": 80},
    {"artist": "Carrie Underwood", "title": "Before He Cheats", "year": 2005, "genre": "country", "popularity": 79},
    {"artist": "Carrie Underwood", "title": "Blown Away", "year": 2012, "genre": "country", "popularity": 78},
    {"artist": "Johnny Cash", "title": "Hurt", "year": 2002, "genre": "country", "popularity": 76},
    {"artist": "Johnny Cash", "title": "Ring of Fire", "year": 1963, "genre": "country", "popularity": 75},
    {"artist": "Dolly Parton", "title": "Jolene", "year": 1973, "genre": "country", "popularity": 75},
    {"artist": "Dolly Parton", "title": "9 to 5", "year": 1980, "genre": "country", "popularity": 74},
    {"artist": "Shania Twain", "title": "Man! I Feel Like a Woman!", "year": 1997, "genre": "country", "popularity": 78},
    {"artist": "Shania Twain", "title": "You're Still the One", "year": 1997, "genre": "country", "popularity": 77},
    {"artist": "Kacey Musgraves", "title": "Rainbow", "year": 2018, "genre": "country", "popularity": 76},
    {"artist": "Kacey Musgraves", "title": "Butterflies", "year": 2018, "genre": "country", "popularity": 75},
    
    # Latin
    {"artist": "Bad Bunny", "title": "Dakiti", "year": 2020, "genre": "latin", "popularity": 93},
    {"artist": "Bad Bunny", "title": "Callaíta", "year": 2019, "genre": "latin", "popularity": 90},
    {"artist": "Bad Bunny", "title": "Safaera", "year": 2020, "genre": "latin", "popularity": 91},
    {"artist": "J Balvin", "title": "Mi Gente", "year": 2017, "genre": "latin", "popularity": 91},
    {"artist": "J Balvin", "title": "Ginza", "year": 2015, "genre": "latin", "popularity": 88},
    {"artist": "Rosalía", "title": "MALAMENTE", "year": 2018, "genre": "latin", "popularity": 86},
    {"artist": "Rosalía", "title": "Con Altura", "year": 2019, "genre": "latin", "popularity": 87},
    {"artist": "Shakira", "title": "Hips Don't Lie", "year": 2005, "genre": "latin", "popularity": 89},
    {"artist": "Shakira", "title": "Waka Waka", "year": 2010, "genre": "latin", "popularity": 88},
    {"artist": "Luis Fonsi", "title": "Despacito", "year": 2017, "genre": "latin", "popularity": 98},
    {"artist": "Luis Fonsi", "title": "Échame La Culpa", "year": 2017, "genre": "latin", "popularity": 88},
    {"artist": "Daddy Yankee", "title": "Gasolina", "year": 2004, "genre": "latin", "popularity": 87},
    {"artist": "Daddy Yankee", "title": "Limbo", "year": 2012, "genre": "latin", "popularity": 85},
    {"artist": "Karol G", "title": "Tusa", "year": 2019, "genre": "latin", "popularity": 92},
    {"artist": "Karol G", "title": "Bichota", "year": 2020, "genre": "latin", "popularity": 90},
    
    # Alternative/Indie
    {"artist": "Tame Impala", "title": "The Less I Know The Better", "year": 2015, "genre": "alternative", "popularity": 83},
    {"artist": "Tame Impala", "title": "Let It Happen", "year": 2015, "genre": "alternative", "popularity": 81},
    {"artist": "Arctic Monkeys", "title": "505", "year": 2007, "genre": "alternative", "popularity": 81},
    {"artist": "Arctic Monkeys", "title": "Why'd You Only Call Me When You're High?", "year": 2013, "genre": "alternative", "popularity": 82},
    {"artist": "Radiohead", "title": "Creep", "year": 1992, "genre": "alternative", "popularity": 83},
    {"artist": "Radiohead", "title": "Karma Police", "year": 1997, "genre": "alternative", "popularity": 81},
    {"artist": "The Killers", "title": "Mr. Brightside", "year": 2003, "genre": "alternative", "popularity": 85},
    {"artist": "The Killers", "title": "Somebody Told Me", "year": 2004, "genre": "alternative", "popularity": 82},
    {"artist": "Florence + The Machine", "title": "Dog Days Are Over", "year": 2008, "genre": "alternative", "popularity": 79},
    {"artist": "Florence + The Machine", "title": "Shake It Out", "year": 2011, "genre": "alternative", "popularity": 78},
    {"artist": "Lorde", "title": "Royals", "year": 2013, "genre": "alternative", "popularity": 86},
    {"artist": "Lorde", "title": "Green Light", "year": 2017, "genre": "alternative", "popularity": 83},
    {"artist": "Arcade Fire", "title": "Wake Up", "year": 2004, "genre": "alternative", "popularity": 77},
    {"artist": "Arcade Fire", "title": "Reflektor", "year": 2013, "genre": "alternative", "popularity": 76},
    {"artist": "Vampire Weekend", "title": "A-Punk", "year": 2008, "genre": "alternative", "popularity": 75},
    {"artist": "Vampire Weekend", "title": "Harmony Hall", "year": 2019, "genre": "alternative", "popularity": 74},
    {"artist": "Glass Animals", "title": "Heat Waves", "year": 2020, "genre": "alternative", "popularity": 88},
    
    # Classical
    {"artist": "Ludwig van Beethoven", "title": "Symphony No. 5", "year": 1808, "genre": "classical", "popularity": 72},
    {"artist": "Ludwig van Beethoven", "title": "Moonlight Sonata", "year": 1801, "genre": "classical", "popularity": 71},
    {"artist": "Wolfgang Amadeus Mozart", "title": "Eine kleine Nachtmusik", "year": 1787, "genre": "classical", "popularity": 70},
    {"artist": "Wolfgang Amadeus Mozart", "title": "Symphony No. 40", "year": 1788, "genre": "classical", "popularity": 69},
    {"artist": "Johann Sebastian Bach", "title": "Air on the G String", "year": 1731, "genre": "classical", "popularity": 68},
    {"artist": "Johann Sebastian Bach", "title": "Toccata and Fugue in D Minor", "year": 1708, "genre": "classical", "popularity": 67},
    {"artist": "Frédéric Chopin", "title": "Nocturne Op. 9 No. 2", "year": 1832, "genre": "classical", "popularity": 67},
    {"artist": "Frédéric Chopin", "title": "Prelude in E Minor", "year": 1839, "genre": "classical", "popularity": 66},
    {"artist": "Claude Debussy", "title": "Clair de Lune", "year": 1905, "genre": "classical", "popularity": 69},
    {"artist": "Claude Debussy", "title": "Prelude to the Afternoon of a Faun", "year": 1894, "genre": "classical", "popularity": 67},
    
    # Jazz
    {"artist": "Miles Davis", "title": "So What", "year": 1959, "genre": "jazz", "popularity": 65},
    {"artist": "Miles Davis", "title": "Blue in Green", "year": 1959, "genre": "jazz", "popularity": 64},
    {"artist": "John Coltrane", "title": "Giant Steps", "year": 1960, "genre": "jazz", "popularity": 63},
    {"artist": "John Coltrane", "title": "My Favorite Things", "year": 1961, "genre": "jazz", "popularity": 62},
    {"artist": "Dave Brubeck", "title": "Take Five", "year": 1959, "genre": "jazz", "popularity": 68},
    {"artist": "Dave Brubeck", "title": "Blue Rondo à la Turk", "year": 1959, "genre": "jazz", "popularity": 65},
    {"artist": "Louis Armstrong", "title": "What a Wonderful World", "year": 1967, "genre": "jazz", "popularity": 71},
    {"artist": "Louis Armstrong", "title": "Hello, Dolly!", "year": 1964, "genre": "jazz", "popularity": 69},
    {"artist": "Ella Fitzgerald", "title": "Summertime", "year": 1957, "genre": "jazz", "popularity": 66},
    {"artist": "Ella Fitzgerald", "title": "Dream a Little Dream of Me", "year": 1950, "genre": "jazz", "popularity": 65}
]

def genre_based_tempo(genre):
    genre_tempos = {
        "pop": (95, 130),
        "hip-hop": (85, 110),
        "rock": (110, 140),
        "r&b": (70, 100),
        "electronic": (120, 150),
        "country": (80, 120),
        "latin": (90, 130),
        "alternative": (100, 130),
        "classical": (60, 120),
        "jazz": (70, 140),
    }
    tempo_range = genre_tempos.get(genre, (90, 130))
    return random.randint(tempo_range[0], tempo_range[1])

def genre_based_duration(genre):
    genre_durations = {
        "pop": (180, 240),
        "hip-hop": (180, 250),
        "rock": (200, 280),
        "r&b": (200, 270),
        "electronic": (180, 270),
        "country": (190, 260),
        "latin": (180, 240),
        "alternative": (200, 280),
        "classical": (240, 600),
        "jazz": (240, 360),
    }
    duration_range = genre_durations.get(genre, (180, 240))
    return random.randint(duration_range[0], duration_range[1])

data = []
for i, song in enumerate(real_songs):
    if "tempo" not in song:
        song["tempo"] = genre_based_tempo(song["genre"])
    if "duration" not in song:
        song["duration"] = genre_based_duration(song["genre"])
    
    song_id = f"S{i+1:04d}"
    song["id"] = song_id
    
    data.append(song)

df = pd.DataFrame(data)

df.to_csv("music_dataset.csv", index=False)

print(f"Dataset generated with {len(df)} real songs and saved as 'music_dataset.csv'")
print("\nSample data (first 5 songs):")
print(df.head())

print("\nDataset statistics:")
print(df.describe())

print("\nGenre distribution:")
print(df['genre'].value_counts())

print("\nMissing values count:")
print(df.isnull().sum())

print("\nYear distribution:")
print(df['year'].value_counts().sort_index().head())
print("...")
print(df['year'].value_counts().sort_index().tail())

print("\nTop artists by song count:")
print(df['artist'].value_counts().head(10))