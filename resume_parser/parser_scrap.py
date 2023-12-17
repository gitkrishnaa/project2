# import re
# from pdfminer.high_level import extract_text
import os
# # dict of resume data creating
# Resume_data = {}
import pathlib






def extract_text_from_pdf(pdf_path):
    p = pathlib.Path(__file__)
    print(p)
    f = open(pdf_path, "r")
    print("start ")
    print(pdf_path)
    print(os.path.dirname("../"+pdf_path))
    print(f)
    print("end")
    # return extract_text(pdf_path)

# resume_all_data=extract_text_from_pdf("example")
# Resume_data["all_data"]=resume_all_data

# def extract_contact_number_from_resume(text):
#     contact_number = None
#     # Use regex pattern to find a potential contact number
#     pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
#     match = re.search(pattern, text)
#     if match:
#         contact_number = match.group()
#     return contact_number



# # email extract
# def extract_email_from_resume(text):
#     email = None
#     # Use regex pattern to find a potential email address
#     pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
#     match = re.search(pattern, text)
#     if match:
#         email = match.group()

#     return email

