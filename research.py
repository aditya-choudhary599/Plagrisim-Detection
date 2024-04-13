from scrap import *
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

def gptTopic(abstract:str):


    template = """Question: {question}

    Answer: Give ONE simple title of 3 words of the abstract provided. make sure you are not printing anything else except title."""

    prompt = PromptTemplate.from_template(template)

    llm = OpenAI(openai_api_key="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")

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    output = llm_chain.run(abstract)
    results = search_topic(output)

    return results