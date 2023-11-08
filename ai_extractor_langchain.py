from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, ChatMessage
from langchain.tools import format_tool_to_openai_function, YouTubeSearchTool, MoveFileTool

import os
from open_ai_key import OPENAI_KYE
from custom_functions import candidate_cv_info_extraction
from ai_extractor import student_responce  # replace it with pdf extracted text

os.environ['OPENAI_API_KEY'] = OPENAI_KYE


class Responce_Langchain():
    def __init__(self, function) -> None:
        self.function = function

    def langchain_responce(self,cv_text):
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        response = llm.predict_messages([HumanMessage(content=cv_text)],
                                        functions=self.function)
        
        return response
    
    
# responce = Responce_Langchain(candidate_cv_info_extraction)
# print(responce.langchain_responce(student_responce))
