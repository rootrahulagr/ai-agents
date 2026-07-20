from tools.file_reader import FileReader
import string
from models.document import Document
stop_words = {"what", "is", "the", "a", "an", "how", "do", "i"}


class ResearchAgent:
    """
    Answers questions using the available documents.
    """
    def __init__(self, reader: FileReader):
        self.reader = reader

    def answer_questions(self, question: str) -> str:
        documents = self.reader.read_files()
        print(f"Found {len(documents)} documents.")
        keywords = self._extract_keywords(question)
        scores = self._score_documents(documents, keywords)
        best_document = self._find_best_document(scores)
        if best_document is None:
            return "Sorry, no matching document found."
        return best_document.content 

    def _score_documents(self, documents: list[Document], keywords: list[str]) -> dict[Document, int]:
        """
        This method scores the documents.
        """
        scores = {}
        for document in documents:
            score = 0   # <-- once per document
            for keyword in keywords:
                content = document.content.lower()
                filename = document.filename.lower()
                if keyword in filename:
                    score += 5
                matches = content.count(keyword)    
                if matches > 0:
                    score += matches
            scores[document] = score
        return scores    

    def _find_best_document(self, scores: dict[Document, int]) -> Document | None:
        """
        This method finds the best matching document.
        """
        top_score = -1
        best_document = None
        for document, score in scores.items():
            print(f"{document.filename}: {score}") 
            if score > top_score:
                top_score = score
                best_document = document
        if best_document is not None:        
            print (f"{best_document.filename} has top score {top_score}")   

        if top_score <= 0:
            return None
        else:    
            return best_document 
    
    def _extract_keywords(self, question: str) -> list[str]:
        """
        This method extracts the useful keywords from user question for further document search.
        """
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


