from tools.file_reader import FileReader

#reader = FileReader.read_files

class ResearchAgent:
    """
    Answers questions using the available documents.
    """
    def __init__(self, reader: FileReader):
        self.reader = reader

    def ask(self, question: str) -> str:
        documents = self.reader.read_files()
        print(f"Found {len(documents)} documents.")
        return "Yet to implement"