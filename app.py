from clarifai.client.model import Model
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import os
from langchain.vectorstores import Clarifai
from langchain.chains import RetrievalQA
from clarifai.modules.css import ClarifaiStreamlitCSS
from PyPDF2 import PdfReader 


def text_extractor(upladed_file):

    # creating a pdf reader object 
    reader = PdfReader(upladed_file) 

    # creating an empty list to store the text from each page 
    text_list = []

    # looping over all the pages in the pdf file 
    for page in reader.pages:
        # extracting text from page 
        text = page.extract_text() 
        # appending the text to the list 
        text_list.append(text)
    return text_list


def convert(docs):
    input = docs

    inference_params = dict(voice="alloy", speed=1.0)

    # Model Predict
    # Join the strings in the list with a newline character
    input_string = "\n".join(input)
    # Encode the string to bytes using utf-8
    input_bytes = input_string.encode("utf-8")
    model_prediction = Model("https://clarifai.com/openai/tts/models/openai-tts-1").predict_by_bytes(input_bytes, input_type="text", inference_params=inference_params)

    output_base64 = model_prediction.outputs[0].data.audio.base64
    audio_filename = f"output_audio.wav"
    with open(audio_filename, 'wb') as f:
        f.write(output_base64)
    return audio_filename



def main():
    st.text("Upload File or Enter Text") 
    with st.sidebar:
        st.subheader("Add PAT key ")
        Clarfai_PAT = st.text_input("Enter Your Clarafai_Pat Key", type="password")
    uploaded_File = st.file_uploader("Upload a pdf file here")
    upload_Text = st.text_area("Write text you want to hear")
    if not Clarfai_PAT:
        st.info("Please add your Clarifai PAT to continue.")
    else:
        os.environ["Clarfai_PAT"] = "Clarifai_PAT"
        if not (upload_Text or uploaded_File):
            st.info("Please Upload a file or write a text")
        elif st.button("Get the response"):
            with st.spinner("Processing"):
                if uploaded_File:
                    chunked_documents = text_extractor(uploaded_File)
                    response = convert(chunked_documents)
                    st.audio(response)

                elif upload_Text:
                    response = convert(upload_Text)
                    st.audio(response)
                elif uploaded_File and upload_Text:
                    chunked_documents = text_extractor(uploaded_File)
                    resp1 = convert(chunked_documents)
                    st.audio(resp1)
                    resp2 = convert(resp2)
                    st.audio(resp2)
             
if __name__ == '__main__':
    main()


