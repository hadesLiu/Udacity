# -*- coding: utf-8 -*-
# author: hiro
import urllib


def open_text():
    quotes = open("C:\Users\Administrator\Desktop\Udacity\p2\movie-quotes\movie_quotes\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()


open_text()