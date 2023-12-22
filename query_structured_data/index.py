from dotenv import load_dotenv
load_dotenv()
from setup import sql_database
from llama_index.indices.struct_store import NLSQLTableQueryEngine

query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    tables=["city_stats"],
)
query_str = "Which city has the highest population?"
response = query_engine.query(query_str)

print(response)

