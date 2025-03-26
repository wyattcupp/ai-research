from typing import TypedDict, List, Annotated
from langchain_core.messages import AnyMessage, add_messages
from langgraph.graph.message import add_messages

class RagIngestionState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]
    document_texts: List[str]  # List of all document contents
    document_ids: List[str]    # List of document IDs
    insights: List[str]        # Combined insights from all documents
    concepts: List[str]        # Concepts distilled from all insights
    themes: List[str]          # Themes distilled from all concepts