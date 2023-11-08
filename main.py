from ai_extractor import *
from custom_functions import candidate_cv_info_extraction
from resume_extractor import Extracting_Resume_Data

db = connect_to_mongodb()
collection_name = "yourCollection" # replace yourCollection with your Database Collection
collection = db[collection_name]
pdf_dir = 'your pdf directory'

extract_resume = Extracting_Resume_Data()
extract_resume.extracting_text(pdf_dir)
extract_resume.store_data(collection)

result = collection.find({})
def  main():
    for document in result:
        string_text = str(document['Resume Data'])
        CV_info_extraction(string_text,candidate_cv_info_extraction,collection)

if __name__ == "__main__":
    main()