from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv
from langchain.chains import create_history_aware_retriever

load_dotenv()


def run_llm(query: str, chat_history: list, openai_key: str):
    # Initialize embeddings and retriever
    embeddings = OpenAIEmbeddings(api_key=openai_key)
    docs_db = Chroma(persist_directory="../data/sklearn_docs_db", embedding_function=embeddings)
    chat = ChatOpenAI(verbose=True, temperature=0.0, model="gpt-4o-mini", api_key=openai_key)

    retriever = docs_db.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    # Create the history-aware retriever
    history_prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
        ("user", "Rephrase the above input into a standalone query that can be used for retrieval.")
    ])
    history_retriever = create_history_aware_retriever(llm=chat, retriever=retriever, prompt=history_prompt)

    # Document prompt
    doc_prompt = ChatPromptTemplate.from_template("""
    Use the following context to answer the question:
    Context: {context}
    
    Question: {input}
    Chat History: {chat_history}
    
    You are an expert on scikit-learn (sklearn) and your purpose is to help users with scikit-learn related questions only. You can discuss related libraries like pandas and numpy and topics relates to scikit learn like machine learning and dimensionality reduction, and related to the context of how they work with scikit-learn. If a question is not related to scikit-learn r any tipic that surrounds it, politely decline to answer and remind the user that you can only help with scikit-learn related topics.
    """)

    # Create document chain
    document_chain = create_stuff_documents_chain(
        llm=chat,
        prompt=doc_prompt
    )

    # Create retrieval chain
    retrieval_chain = create_retrieval_chain(
        retriever=history_retriever,
        combine_docs_chain=document_chain
    )

    # Run the chain
    result = retrieval_chain.invoke(input={
        "input": query,
        "chat_history": chat_history
    })

    return result["answer"]