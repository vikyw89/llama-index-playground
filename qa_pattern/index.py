from llama_index import (
    ServiceContext,
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage
)
# construct vector store
from dotenv import load_dotenv

load_dotenv()


# try loading index from storage
index = None
try:
    index = load_index_from_storage(
        storage_context=StorageContext.from_defaults(persist_dir="./qa_pattern/storage")
    )
except Exception as e:
    # create index
    documents = SimpleDirectoryReader("./qa_pattern/data").load_data()

    # from llama_index.node_parser import SentenceWindowNodeParser
    # node_parser = SentenceWindowNodeParser.from_defaults(
    #     window_size=3, window_metadata_key="window", original_text_metadata_key="original_sentence"
    # )
    # nodes = node_parser.get_nodes_from_documents(documents=documents)

    # from llama_index.text_splitter import SentenceSplitter
    # node_parser = SentenceSplitter(
    #     chunk_size=2048,
    #     chunk_overlap=25,
    #     paragraph_separator="\n\n",
    # )
    from llama_index.node_parser import SentenceWindowNodeParser, SentenceSplitter
    
    node_parser = SentenceSplitter.from_defaults(
        chunk_overlap=25,
        paragraph_separator="\n\n",
        chunk_size=2048
    )
    
    nodes = node_parser.get_nodes_from_documents(documents)

    index = VectorStoreIndex(nodes=nodes)

    # persist index
    index.storage_context.persist(persist_dir="./qa_pattern/storage")

from llama_index.retrievers import BM25Retriever,QueryFusionRetriever,VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine, SubQuestionQueryEngine, BaseQueryEngine
from llama_index.tools.query_engine import QueryEngineTool

bm25_retriever = BM25Retriever.from_defaults(
    index=index
)

vector_retriever = VectorIndexRetriever(
    index=index
)

retriever = QueryFusionRetriever(
    retrievers=[
        vector_retriever
    ]
)

fusion_query_engine = RetrieverQueryEngine.from_args(
    retriever=retriever
)

query_engine = fusion_query_engine

# response = query_engine.query("What are things that should be included in a basic plan ?")
response = query_engine.retrieve("basic plan requirements")
print(response)