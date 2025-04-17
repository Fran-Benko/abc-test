# data/document_loader.py
from typing import List

class DocumentLoader:
    @staticmethod
    def load_documents(file_paths: List[str]) -> List[str]:
        """Load documents from provided file paths."""
        docs_content = []
        for path in file_paths:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    docs_content.append(f.read())
            except Exception as e:
                print(f"Error reading document {path}: {e}")
        return docs_content