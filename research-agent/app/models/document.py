class Document:
    """
    Represents a document that can be processed
    by the Research Agent.
    """
    def __init__ (self, filename: str, filepath: str, content: str, file_size: int, extension: str, metadata: dict):
        self.filename = filename
        self.content = content
        self.filepath = filepath 
        self.file_size = file_size
        self.extension = extension
        self.metadata = metadata

