from pdfminer.high_level import extract_text
import docx2txt
import nltk
import pandas as pd
import os

# RETRIEVING SKILLS

CSV_PATH = 'skills.csv'
df = pd.read_csv(CSV_PATH)
df['skill_name'] = df['skill_name'].str.replace('-', ' ')
skill_set = set(df['skill_name'])

nltk.download('stopwords')
nltk.download('punkt')
# Checking for pdf or docs
def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower()

def extract_text_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None


def extract_skills(input_text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)
    #remove the stop words
    filtered_tokens = [w for w in word_tokens if w not in stop_words]

    filtered_tokens = [w for w in word_tokens if w.isalpha()]

    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens,2,3)))

    found_skills = set()

    for token in filtered_tokens:
        if token.lower() in skill_set:
            found_skills.add(token)
    
    for ngram in bigrams_trigrams:
        if ngram.lower() in skill_set:
            found_skills.add(ngram)
    
    return found_skills

def extract_skills_from_resume(text_path):
    #text_path = input('Enter Resume Path: ') 
    text = ''
    if get_file_extension(text_path) == '.docx':
        text = extract_text_from_docx(text_path)

    elif get_file_extension(text_path) == '.pdf':
        text = extract_text_pdf(text_path)
    skills = extract_skills(text)
    return skills

def matching_skills(res_path, job_desc): # job_desc is a string
    matched = {} # set of matched jobs
    res_skills = extract_skills_from_resume(res_path)
    job_skills = extract_skills(job_desc)
    for skill in job_skills:
        if skill in res_skills:
            matched.add(skill)
    return matched

def missing_skills(res_path, job_desc):
    missing = {}
    res_skills = extract_skills_from_resume(res_path)
    job_skills = extract_skills(job_desc)
    for skill in job_skills:
        if skill not in res_skills:
            missing.add(skill)
    return missing

def skillmatch(len_skills1, len_skills2):
    return ( len_skills2 // len_skills2 ) * 100 if len(skillset2) > 0 else 0

