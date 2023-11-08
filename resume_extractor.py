import fitz
import os
import re
from db_connection import connect_to_mongodb

class Extracting_Resume_Data:
    """
    A class for extracting text data from PDF resumes and storing it in a MongoDB collection.

    Attributes:
    - data (dict): A dictionary to store extracted resume data.

    Methods:
    - preprocess_text(text): Preprocesses the given text by converting it to lowercase, removing special characters, and extra spaces.
    - extracting_text(pdf_dir): Extracts text from PDF files in the specified directory and preprocesses it.
    - store_data(collection): Stores the preprocessed resume data in a MongoDB collection.
    """

    data = {}

    def preprocess_text(self, text):
        """
        Preprocesses the given text by converting it to lowercase, removing special characters, and extra spaces.

        Args:
        - text (str): The text to be preprocessed.

        Returns:
        - str: The preprocessed text.
        """
        text = text.lower()
        text = re.sub(r"[^A-Za-z0-9.\s]+", "", text)
        text = re.sub(r"�", " ", text)
        text = " ".join(text.split())
        return text

    def extracting_text(self, pdf_dir):
        """
        Extracts text from PDF files in the specified directory and preprocesses it.

        Args:
        - pdf_dir (str): The directory containing PDF files.

        Returns:
        - None
        """
        for filename in os.listdir(pdf_dir):
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(pdf_dir, filename)
                pdf_document = fitz.open(pdf_path)
                text = ""
                for page in pdf_document:
                    text += page.get_text()
                clean_text = self.preprocess_text(text)
                self.data[filename] = [clean_text]
                pdf_document.close()
                os.remove(pdf_path)

    def store_data(self, collection):
        """
        Stores the preprocessed resume data in a MongoDB collection.

        Args:
        - collection: The MongoDB collection to store the data.

        Returns:
        - None
        """
        for filename, content in self.data.items():
            document = {"Resume Data": content}
            collection.insert_one(document)
