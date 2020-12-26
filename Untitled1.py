#!/usr/bin/env python
# coding: utf-8



#For NLP operations,we use spacy and NLTK(stopwords en_core_web_sm)
import spacy
import en_core_web_sm
import pandas as pd#For dataframe we use pandas
#ResumeParser is used for extracting information from resume
from pyresparser import ResumeParser
en_core_web_sm.load()
import os#OS is used for file operations

#filelist will contain every resume of resumes folder
filelist = os.listdir('resumes/')
df=pd.DataFrame()#df is initialized as blank dataFrame
#I am using k here for just visualize that which resume is processing
k=1
for j in filelist:
    #this condition is ignore .ipynb_chekpoints file,which id automatically generated in resumes folder
    if j!=".ipynb_checkpoints":
        print('resume '+str(k)+' processing')
        data=ResumeParser('resumes/'+j).get_extracted_data()#for data extraction from resume
        for i in data:#converting list into string by joining ',' . It is skills sections of resume
            if type(data[i])==list:
                listToStr = ','.join([str(elem) for elem in data[i]])
                data[i]=listToStr
        df=df.append(data,ignore_index=True)#appending every row in dataframe
        k=k+1
df=df[["name", "email","mobile_number", "degree","experience", "designation", "skills","college_name", "company_names",
        "mobile_number",  "no_of_pages",
       "total_experience"]]#rearranging the columns of dataframe
df
df.to_excel("output.xlsx")#dataFrame to excel file onversion







