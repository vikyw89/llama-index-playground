from llama_index import VectorStoreIndex, download_loader

SimpleWebPageReader = download_loader("SimpleWebPageReader")

loader = SimpleWebPageReader()


def web_scrapper(url:str,query:str):
    key = f"{url}-{query}"
    index = None
    try:
        from llama_index import load_index_from_storage, StorageContext
        index = load_index_from_storage(storage_context=StorageContext.from_defaults(persist_dir=f"./web_scrapper/storage/{key}"))
    except Exception as e:
        documents = loader.load_data(urls=[url])
        print(documents)
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(f"./web_scrapper/storage/{key}")
    query_engine = index.as_query_engine()
    res = query_engine.query(query)
    return res