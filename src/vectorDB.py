import os
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
import pinecone

from config import * 
from utils import *

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

class VectorDB():
    def __init__(self, DB_name):
        self.DB_name = DB_name
        self.pinecone = pinecone.Pinecone(
                        api_key=PINECONE_API_KEY,
                        environment=PINECONE_API_ENVIRONMENT)
        self.embeddings = OpenAIEmbeddings(client='')
        
    def create_DB(self, data):
        # First, check if our index already exists. If it doesn't, we create it
        print('Checking if index exists...')
        try:
            if self.DB_name not in self.pinecone.list_indexes():
                print('Index does not exist, creating index...')
                # we create a new index
                self.pinecone.create_index(
                    name=self.DB_name,
                    metric='cosine',
                    # The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`
                    dimension=embedding_dim,
                    spec=pinecone.ServerlessSpec(
                        cloud='aws', 
                        region='us-east-1'
                    )
                )
            else:
                print(f"Index {self.DB_name} already exists.")
        except pinecone.exceptions.PineconeException as e:
            if 'ALREADY_EXISTS' in str(e):
                print(f"Index {self.DB_name} already exists.")
            else:
                raise e
        PineconeVectorStore.from_documents(data, self.embeddings, index_name=self.DB_name)
        
    def reset_DB(self):
        docsearch = PineconeVectorStore.from_existing_index(
                index_name=self.DB_name, embedding=self.embeddings)
        docsearch.delete(delete_all = True)

    def search_DB(self, query):
        docsearch = PineconeVectorStore.from_existing_index(
                    index_name=self.DB_name, embedding=self.embeddings)
        search_result = docsearch.similarity_search(query, k = top_K)
        return search_result
