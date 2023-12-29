from dotenv import load_dotenv
# load_dotenv()

# from web_scrapper.index import web_scrapper
# res = web_scrapper(query="New York was named in honor of whom ?", url="https://en.wikipedia.org/wiki/New_York_City?wprov=srpw1_1")

from wikipedia_tool.index import wikipedia

res = wikipedia("what day is today ?")
print(res)