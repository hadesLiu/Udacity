import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268/sign=52d1d685908fa0ec7fc7630b1e97594a/d62a6059252dd42a1835151d023b5bb5c9eab843.jpg",
                        "http://www.iqiyi.com/v_19rrjvhmyg.html")

# print toy_story.storyline
avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike220%2C5%2C5%2C220%2C73/sign=8983a693612762d09433acedc185639f/eaf81a4c510fd9f9f7454cd9272dd42a2834a42b.jpg",
                     "http://www.iqiyi.com/w_19rrbhbep5.html")

# print avatar.storyline
# avatar.show_trailer()
mermaid = media.Movie("The Mermaid",
                     "A mermaid in the ocean.",
                     "https://gss1.bdstatic.com/-vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike150%2C5%2C5%2C150%2C50/sign=889d3311b5b7d0a26fc40ccfaa861d6c/8d5494eef01f3a29085c8a6d9e25bc315d607cf8.jpg",
                     "http://www.iqiyi.com/v_19rrlbd3sc.html")

# mermaid.show_trailer()

# movies = [toy_story, avatar, mermaid]
# fresh_tomatoes.open_movies_page(movies)
print media.Movie.__name__
print media.Movie.__module__