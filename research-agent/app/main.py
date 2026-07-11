from tools import file_reader

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

