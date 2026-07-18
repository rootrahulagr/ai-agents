import os
from models.document import Document

class FileReader:
    def __init__(self, folder_name, file_extension, max_size):
          self.folder_name = folder_name
          self.file_extension = file_extension
          self.max_size = max_size

    def read_files(self) -> list[Document]:
            """
            Read all matching files from a folder and return them
            as Document objects.
            """
            documents = []
            for filename in os.listdir(self.folder_name):
                full_path = os.path.join(self.folder_name, filename)
                size = os.path.getsize(full_path)
                if (os.path.isfile(full_path) and filename.endswith(self.file_extension) and size <= self.max_size):
                        with open(full_path, "r", encoding="utf-8") as f:
                            document = Document(
                                  filename = filename,
                                  filepath = full_path,
                                  content = f.read(),
                                  file_size = size,
                                  extension = self.file_extension,
                                  metadata = dict()
                            )      
                        documents.append(document)
            return documents
'''
    def read_files(self, folder_name, file_extension, max_size) -> list[Document]:
            """
            Read all matching files from a folder and return them
            as Document objects.
            """
            final_documents = []
            for filename in os.listdir(folder_name):
                full_path = os.path.join(folder_name, filename)
                if (os.path.isfile(full_path) and filename.endswith(file_extension) and os.path.getsize(full_path) <= max_size):
                        with open(full_path, "r", encoding="utf-8") as f:
                            document = Document(filename, f.read())
                        final_documents.append(document)
            return final_documents
'''

