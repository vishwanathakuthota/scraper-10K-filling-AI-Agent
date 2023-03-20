import numpy as np
import pandas as pd
import os
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity
from itertools import chain

#import test tickers

def directory_termination(years, file_type):
    dir_path_termination = []
    for t in file_type:
        dir_path_termination.append(map(lambda x: ''.join([str(x), "_", str(t)]), years))
    result = chain.from_iterable(dir_path_termination)
    result = list(result)
    return result

def company_files(dir_path, company_cik):
    company_file_termination = []
    for c in company_cik:
        company_file_termination.append(list(map(lambda x: ''.join([str(x), "_", str(c), ".txt"]), dir_path)))
    result = chain.from_iterable(company_file_termination)
    result = list(result)
    return result

def get_text(filenames):
    clean_text = []
    for f in filenames:
        text_file = open(f, "r")
        lines = text_file.readlines()
        sorted_text = sorted(lines, key=lambda x: len(x), reverse=True)
        #since the text is ordered by length, a less strict regex seems worthwhile
        indices = [i for i, elem in enumerate(sorted_text) if re.search('ANNUAL\s*REPORT\s*PURSUANT\s*', elem, re.IGNORECASE)]
        #if indices has non zero length
        if(indices):
            index = indices[0]
            clean_text.append(sorted_text[index])
        else:
            clean_text.append("Error")
    return clean_text

def vector_analysis(filenames):
    cleaned_text = get_text(filenames)
    if(not "Error" in cleaned_text):
        vectorizer = CountVectorizer(cleaned_text)
        dtm = vectorizer.fit_transform(cleaned_text)
        vocab = vectorizer.get_feature_names()
        dtm = dtm.toarray()
        vocab = np.array(vocab)
        n, _ = dtm.shape
        dist = np.zeros((n, n))
        dist = cosine_similarity(dtm)
        first_diag = np.diag(dist, k=-1)
        return first_diag
    else:
        return [np.nan]*(len(years)-1)

###############################################################################################

#######
#get cik's. they get read as floats, so cast them to int
#clean this up using pandas
csv = np.genfromtxt ("yourfile.csv", delimiter=",")

relevant_cik0 = csv[:,1]
relevant_cik1 = relevant_cik0[~np.isnan(relevant_cik0)]
relevant_cik = list(map(lambda x: int(x), relevant_cik1))
#######

base_dir = "/Users/your_path to the file"
years = [2013, 2014, 2015, 2016] #dates
#cik = [766421, 1325955, 897077, 1545654]
cik = relevant_cik
#cik = [766421]
#file_types = ["10-K", "10-Q"]
file_types = ["10-K"]

upper_dir = directory_termination(years, file_types)
file_names = company_files(upper_dir, cik)
file_paths = list(map(lambda x: ''.join([base_dir, str(x)]), file_names))

cosine_similarity_measure = []
for c in cik:
    #relevant_files = filter(lambda x:str(file_types[0])+"_"+str(c) in x, file_paths)
    relevant_files = []
    for f in file_paths:
        if str(str(file_types[0])+"_"+str(c)) in f:
            relevant_files.append(f)
    if(all(map(os.path.isfile,relevant_files))):
        cosine_similarity_measure.append(vector_analysis(relevant_files))
    else:
        statement = ''.join(["cik with no file: ", str(c)])
        print(statement)
        cosine_similarity_measure.append([np.nan]*(len(years)-1))

results = pd.DataFrame(data = cosine_similarity_measure, index = cik)
results.columns = years[1:len(years)]
results
