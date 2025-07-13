from semantic_splitter.reader import DocxReader
from semantic_splitter.semantic.anchors import AnchorFinder

class SemanticPipeline:
    def __init__(self):
        self.reader = DocxReader()
        self.anchor_finder = AnchorFinder()

    def run(self, file_path: str):
        doc_content = self.reader.read(file_path)
        response = self.anchor_finder.run(doc_content)
        for anchor in response.anchor_sentences:
            doc_content = doc_content.replace(anchor, f"<new-chunk>{anchor}")
        chunks = doc_content.split("<new-chunk>")
        chunks = [chunk.strip() for chunk in chunks if len(chunk.strip()) > 0]
        return chunks