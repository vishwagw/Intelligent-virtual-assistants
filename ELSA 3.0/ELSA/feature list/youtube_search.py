# searching on youtube using voice command:
import webbrowser, urllib, re
import urllib.parse
import urllib.request

domain = input("Enter the song name: ")
song = urllib.parse.urlencode({"search_query" : domain})
print("song" + song)

#fetch the ?=query
result = urllib.request.urlopen("http://www.youtube.com/results?" + song)
print(result)

#make the url of the first song result
search_results = re.findall(r'href=\"\/watch\?v=(.{4})', result.read().decode())
print(search_results)

#make the final url of the song seleects the very first result from the YT.
url = "http://www.youtube.com/watch?v="+str(search_results)

#play the song using web browesr module.
webbrowser.open_new(url)
