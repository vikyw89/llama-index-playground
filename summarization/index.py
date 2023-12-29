from dotenv import load_dotenv

load_dotenv()

from llama_index import SimpleDirectoryReader, StorageContext, load_index_from_storage

import os.path
from llama_index import (
    SimpleDirectoryReader,
    SummaryIndex
)

index = None
try:
    storage_context = StorageContext.from_defaults(persist_dir="./summarization/storage")
    index = load_index_from_storage(storage_context)
except Exception as e:
    documents = SimpleDirectoryReader("./summarization/data").load_data()
    index = SummaryIndex.from_documents(documents)
    index.storage_context.persist("./summarization/storage")
    
query_engine = index.as_query_engine(response_mode="tree_summarize")
response = query_engine.query("<summarization_query>")

print(response)