# coding=utf-8
"""
定义一个电影类，类里面，定义了初始化函数，和 打开电影预告片的函数
"""

import webbrowser

class Movie():
    """
    定义一个电影类，用于后续的实例化
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        类实例化时调用的初始化函数

        :param movie_title: 电影的名称
        :param movie_storyline: 电影的故事情节
        :param poster_image: 电影的海报
        :param trailer_youtube: 电影的预告片链接
        :return: None
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        类函数，打开电影预告片链接

        :return: None
        """
        webbrowser.open(self.trailer_youtube_url)