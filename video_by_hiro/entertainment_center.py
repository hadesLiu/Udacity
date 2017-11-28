# coding=utf-8
"""
初始化几个电影类的实例，用于生成一个电影网站
"""
import fresh_tomatoes
import media



wolf_warriors_2 = media.Movie("Wolf Warriors 2",
                        "A adventurous story of a soldier and a doctor in Africa.",
                        "https://upload.wikimedia.org/wikipedia/zh/thumb/b/b5/Wolf_Warriors_2_poster.jpeg/220px-Wolf_Warriors_2_poster.jpeg",
                        "https://www.youtube.com/watch?v=_8lFurPtxRY") # noqa

mermaid = media.Movie("The Mermaid",
                     "A mermaid in the ocean.",
                     "https://upload.wikimedia.org/wikipedia/zh/4/47/The_Mermaid_2016_poster.jpg",
                     "https://www.youtube.com/watch?v=PWOJLh9yVqc") # noqa

kung_fu = media.Movie("Kung Fu Hustle",
                     "A inspirational story of kung fu.",
                     "https://upload.wikimedia.org/wikipedia/zh/0/05/Kung_Fu_Hustle.jpg",
                     "https://www.youtube.com/watch?v=IdJVVVstGoo") # noqa

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/zh/d/dc/Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=5bMDPpxNbys") # noqa

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/zh/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=dHRIVioj8l0") # noqa


school_of_rock = media.Movie("School of Rock",
                     "A Comedy story in school.",
                     "https://upload.wikimedia.org/wikipedia/zh/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                     "www.youtube.com/watch?v=3PsUJFEBC74") # noqa



movies = [wolf_warriors_2, mermaid, kung_fu, toy_story, avatar, school_of_rock]
fresh_tomatoes.open_movies_page(movies)