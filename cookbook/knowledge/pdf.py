from phi.assistant import Assistant
from phi.knowledge.pdf import PDFKnowledgeBase, PDFReader
from phi.vectordb.pgvector import PgVector2

from resources import vector_db  # type: ignore

# Create a knowledge base with the PDFs from the data/pdfs directory
knowledge_base = PDFKnowledgeBase(
    path="data/pdfs",
    vector_db=PgVector2(
        collection="pdf_documents",
        # Can inspect database via psql e.g. "psql -h localhost -p 5432 -U ai -d ai"
        db_url=vector_db.get_db_connection_local(),
    ),
    reader=PDFReader(chunk=True),
)

# Create an assistant with the knowledge base
assistant = Assistant(
    knowledge_base=knowledge_base,
    add_references_to_prompt=True,
)
# Load the knowledge base
assistant.knowledge_base.load(recreate=False)

# Ask the assistant about the knowledge base
assistant.print_response("Ask me about something from the knowledge base", markdown=True)
