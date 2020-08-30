import streamlit as st
import pandas as pd
import os

st.title("Skillshop chatbot Admin")

choices = ['View Dataset', 'Add Queires', 'Add Responses']
tags = ['timing', 'menu', 'offers', 'delivery', 'address', 'combo']

# files that are going to store the data
Q_DATASET = 'query_dataset.csv'
R_DATASET = 'bot_response_dataset.csv'

qdf = None
rdf = None


if os.path.exists(Q_DATASET) :
    qdf =pd.read_csv(Q_DATASET)

if os.path.exists(R_DATASET) :
    rdf = pd.read_csv(R_DATASET)



userchoice = st.sidebar.selectbox("menu", choices)

if userchoice == choices[0] :
    st.header("Select a dataset")
    # code section for displying data
    if isinstance(qdf, pd.DataFrame):
        if st.sidebar.checkbox('View query dataset'):
            st.table(qdf)
    if isinstance(rdf, pd.DataFrame):
        if st.sidebar.checkbox('View responses dataset'):
            st.table(rdf)
elif userchoice == choices[1] :
    st.header("Add new customer queries")
    # code selection for adding queries
    dataset = []
    question = st.text_input("A customer query")
    tag = st.selectbox('select a tag', tags)
    clicked = st.button("save this")
    if clicked and question:
        data = {'query':question, 'tag':tag}
        dataset.append(data)
        tempdf = pd.DataFrame(dataset)
        if isinstance(qdf, pd.DataFrame) :
            # save to existing file
            qdf = qdf.append(tempdf)
            qdf.to_csv(Q_DATASET,index=False)
            st.success("Query saved successfully")
        else :
            # only runs for the very first time
            tempdf.to_csv(Q_DATASET, index=False)
            st.success("Query saved successfully")
else :
    st.header("Add new bot response")
    # code section for adding response
    rdataset = [] 
    tag = st.selectbox('Select a tag', tags)
    response = st.text_input("Responses")
    click = st.button("Save this")
    if click and response :
        r_data = {'response': response, 'tag': tag}
        rdataset.append(r_data)
        r_tempdf = pd.DataFrame(rdataset)
        if isinstance(rdf, pd.DataFrame) :
            rdf = rdf.append(r_tempdf)
            rdf.to_csv(R_DATASET, index=False)
            st.success("Responsed save successfully")
        else :
            r_tempdf.to_csv(R_DATASET, index=False)
            st.success("Response save successfully")