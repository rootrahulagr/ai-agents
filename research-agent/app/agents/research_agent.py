from tools.file_reader import FileReader
import string
#reader = FileReader.read_files
stop_words = {"what", "is", "the", "a", "an", "how", "do", "i"}
#useful_words = []

class ResearchAgent:
    """
    Answers questions using the available documents.
    """
    def __init__(self, reader: FileReader):
        self.reader = reader

    def ask(self, question: str) -> str:
        scores = {}
        documents = self.reader.read_files()
        print(f"Found {len(documents)} documents.")
        
        keywords = self._extract_keywords(question)

        for document in documents:
            score = 0   # <-- once per document
            for keyword in keywords:
                
                if keyword in document.filename.lower():
                    score += 5
                if keyword in document.content.lower():
                    score += 1
            scores[document.filepath] = score

        for path, score in scores.items():
            print(f"{path}: {score}")    

        return "yet to be implemented"            
    
    def _extract_keywords(self, question: str) -> list[str]:
        useful_words = []
        # Create a translation table that removes punctuation
        translator = str.maketrans("", "", string.punctuation)
        # Remove punctuation
        clean_question = question.translate(translator)
        clean_question = clean_question.lower()
        words = clean_question.split()

        for word in words:
            if word not in stop_words:
                useful_words.append(word)

        return useful_words       


