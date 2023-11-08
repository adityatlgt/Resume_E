import openai
import json
from db_connection import connect_to_mongodb

openai.api_key = "Add your OPENAI_API key here"

class Responce:
    """
    A class for generating responses using OpenAI Chat API and extracting information about token usage.

    Attributes:
    - model (str): The OpenAI language model to use (default is "gpt-3.5-turbo").
    - role (str): The role for messages in the conversation.
    - temperature (float): The sampling temperature for response generation.
    - token_count (bool): Flag to indicate whether to include token count information.
    - function_call (str): The type of function call (default is 'auto').

    Methods:
    - func_responce(messages, function=None): Generates a response using OpenAI Chat API with optional custom function.
    - token_used(response): Extracts the total tokens used from the OpenAI API response.
    """

    def __init__(self, role: str, temperature: float = 1.0, max_tokens: int = 2000, model: str = None, token_count: bool = True) -> None:
        """
        Initializes the Responce object.

        Args:
        - role (str): The role for messages in the conversation.
        - temperature (float): The sampling temperature for response generation.
        - max_tokens (int): The maximum number of tokens for response generation.
        - model (str): The OpenAI language model to use (default is "gpt-3.5-turbo").
        - token_count (bool): Flag to indicate whether to include token count information (default is True).

        Returns:
        - None
        """
        if model:
            self.model = model
        else:
            self.model = "gpt-3.5-turbo"
        self.role = role
        self.temperature = temperature
        self.token_count = token_count
        self.function_call = 'auto'

    def func_responce(self, messages, function=None):
        """
        Generates a response using OpenAI Chat API with optional custom function.

        Args:
        - messages (str): The input messages for the conversation.
        - function: The custom function to be applied (default is None).

        Returns:
        - dict: The OpenAI API response.
        """
        if function:
            return openai.ChatCompletion.create(model=self.model, messages=[{'role': self.role, 'content': messages}],
                                                temperature=self.temperature,
                                                # max_tokens=max_tokens,
                                                functions=function,
                                                function_call=self.function_call)
        else:
            return openai.ChatCompletion.create(model=self.model, messages=[{'role': self.role, 'content': messages}])

    def token_used(self, response):
        """
        Extracts the total tokens used from the OpenAI API response.

        Args:
        - response (dict): The OpenAI API response.

        Returns:
        - int: The total number of tokens used.
        """
        return response['usage']['total_tokens']

def save_responce_db(json_response, collection):
    """
    Saves the OpenAI API response as JSON to a MongoDB collection.

    Args:
    - json_response (dict): The OpenAI API response in JSON format.
    - collection: The MongoDB collection to store the JSON response.

    Returns:
    - None
    """
    records_to_update = collection.find({})
    for record in records_to_update:
        updated_record = {**record, **json_response}
        filter_criteria = {"_id": record["_id"]}
        collection.update_one(filter_criteria, {"$set": updated_record})

def CV_info_extraction(cv_text, functions, collection):
    """
    Extracts information from a CV text using OpenAI Chat API and stores the response in a MongoDB collection.

    Args:
    - cv_text (str): The CV text for information extraction.
    - functions: The custom functions to be applied during response generation.
    - collection: The MongoDB collection to store the response.

    Returns:
    - int: The total number of tokens used in the response.
    """
    res = Responce('user', temperature=0.7)
    response = res.func_responce(cv_text, functions)
    token = res.token_used(response)

    try:
        json_response = json.loads(response['choices'][0]['message']['function_call']['arguments'])
        save_responce_db(json_response, collection)
    except:
        print("FUNCTION CALL NOT FOUND")

    return token
