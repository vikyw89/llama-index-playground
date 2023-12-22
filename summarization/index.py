from dotenv import load_dotenv

load_dotenv()

from llama_index import SimpleDirectoryReader

import os.path
from llama_index import (
    SimpleDirectoryReader,
    SummaryIndex
)


documents = SimpleDirectoryReader("data").load_data()
index = SummaryIndex.from_documents(documents)


query_engine = index.as_query_engine(response_mode="tree_summarize")
response = query_engine.query("<summarization_query>")

print(response)