#from tools import file_reader
#import os
#print(os.getcwd())


from agents.research_agent import ResearchAgent
from tools.file_reader import FileReader

reader = FileReader(
    folder_name="documents",
    file_extension=".txt",
    max_size=1000
)

agent = ResearchAgent(reader)
answer = agent.answer_questions("What is python")
print(answer)

#documents = reader.read_files()



'''
reader = file_reader.FileReader()
MAX_FILE_SIZE = 1000

try:
    documents = reader.read_files("../documents", ".txt", MAX_FILE_SIZE)
    for index, document in enumerate(documents, start=1):
        print(f"Document {index}")
        print(f"Filename: {document.filename}")
        print(f"Content:\n{document.content}")
        print("-" * 40)
except FileNotFoundError:
    print("I couldn't find documents")
except Exception as e:
    print(f"Exception {e}")

reader = file_reader.FileReader()

class ResearchAgent:
    """
    This class is to accept questions, analyse available documents and answer accordingly.
    """
    def __init__(self, reader):
        self.reader = reader

    def answer(self, question):
        for srting in question:  
'''

