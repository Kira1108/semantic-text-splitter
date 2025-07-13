from markitdown import MarkItDown
from pathlib import Path
from typing import Dict
import logging
logger = logging.getLogger(__name__)


class DocxReader:
    
    def read(self, fpath:str | Path) -> str:
        
        md = MarkItDown(enable_plugins=False)
        return md.convert(fpath).markdown
    
    def read_folder(self, folder_path: str | Path) -> Dict[str, str]:
        
        document_folder = Path(folder_path)
        doc_files = document_folder.glob("*.docx")
        
        contents = {}
        for fpath in doc_files:
            try:
                content = self.read_docx(fpath)
                contents[fpath.stem] = content
            except Exception as e:
                logger.warning(f"Error reading file {fpath}: {e}")
                
        return contents

        

        
