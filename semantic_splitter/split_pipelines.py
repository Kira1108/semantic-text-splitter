from semantic_splitter.reader import DocxReader
from semantic_splitter.semantic.anchors import AnchorFinder
from semantic_splitter.rule_based.char_split import langchain_recursive_chinese_split

class SemanticPipeline:
    def __init__(self, trim_long_chunks:bool = False):
        self.reader = DocxReader()
        self.anchor_finder = AnchorFinder()
        self.trim_long_chunks = trim_long_chunks
        
    def split_text(self, text: str):
        response = self.anchor_finder.run(text)
        for anchor in response.anchor_sentences:
            text = text.replace(anchor, f"<new-chunk>{anchor}")
        chunks = text.split("<new-chunk>")
        chunks = [chunk.strip() for chunk in chunks if len(chunk.strip()) > 0]
        
        if not self.trim_long_chunks:
            return chunks
        
        trimmed_chunks = []
        for chunk in chunks:
            if len(chunk) > 1500:
                trimmed_chunks.append(langchain_recursive_chinese_split(chunk, chunk_size=1000, chunk_overlap=100))
            else:
                trimmed_chunks.append([chunk])
        return trimmed_chunks

    def split_docx(self, file_path: str):
        doc_content = self.reader.read(file_path)
        chunks = self.run_text(doc_content)
        return chunks
    

