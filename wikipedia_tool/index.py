from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper

def wikipedia(q:str):
    wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    res = wiki.run(q)
    return res