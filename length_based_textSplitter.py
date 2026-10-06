from langchain_text_splitters import CharacterTextSplitter,RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path='Ayan_Resume_Updated.pdf')
docs = loader.load()

splitter1 = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=20)
splitter2 = RecursiveCharacterTextSplitter(   chunk_size=200,
    chunk_overlap=20,
    separators=["\n\n", "\n", " "])
result1=splitter1.split_documents(docs)
result2=splitter2.split_documents(docs)
print(f'this is simple characterSplitter : {result1[0]}')
print(f'this is  recurisve characterSplitter : {result2}')