from llama_index.tools import FunctionTool
from llama_index import VectorStoreIndex
from llama_index.objects import ObjectIndex, SimpleToolNodeMapping

def multiply(a: int, b: int) -> int:
    """Multiply two integers and returns the result integer"""
    return a * b


def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a + b


def useless(a: int, b: int) -> int:
    """being useless"""
    pass


multiply_tool = FunctionTool.from_defaults(fn=multiply, name="multiply")
add_tool = FunctionTool.from_defaults(fn=add, name="add")
useless_tools = [
    FunctionTool.from_defaults(fn=useless, name=f"useless_{str(idx)}")
    for idx in range(100)
]

all_tools = [multiply_tool] + [add_tool] + useless_tools
all_tools_map = {t.metadata.name: t for t in all_tools}

tool_mapping = SimpleToolNodeMapping.from_objects(all_tools)
obj_index = ObjectIndex.from_objects(
    objects=all_tools,
    object_mapping=tool_mapping,
    index_cls=VectorStoreIndex,
)
