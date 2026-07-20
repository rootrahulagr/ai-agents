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
        top_score = -1
        best_document = None
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
            scores[document] = score

        for document, score in scores.items():
            print(f"{document.filename}: {score}") 
            if score > top_score:
                top_score = score
                best_document = document
        print (f"{best_document.filename} has top score {top_score}")   

        if top_score <= 0:
            return "Sorry, No matching document found."
        else:    
            return best_document.content 
    
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


