from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
import dotenv
dotenv.load_dotenv()


chat = ChatOpenAI()

print("Olá seja bem bindo ao gerador de historias!!!")

print("Primeiro qual seu nome>")

nome = input()

print("Agora, qual o tipo de história você quer participar?")

tema = input().lower()

print("Aproveite sua aventura!!!")

print("Para encerrar a história basta escrever 'Fim'")

content=f"""Você é um gerador de histórias com o tema {tema}, o usuário com o nome de {nome} é o personagem principal da história,
           você deve criar situações onde o usuario tem que tomar decisões,
            baseado nessas decisões você deve continuar a história,
             onde no final deve conter uma decisão para o usuario tomar,
            de modo que induza o usuário o responder de modo que ele descreva a ação,
            você deve sempre criar novas situações baseado na escolha do usuário,
            sempre deve haver mais de duas alternativa,
            todas decisões sobre o curso da história devem ser perguntadas ao usuário e respondidas por ele."""

prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
           content
        ),

        HumanMessagePromptTemplate.from_template("{question}"),
    ]
)

conversation = LLMChain(llm=chat, prompt=prompt, verbose=False)

print(conversation({"question": ""})['text'])

while True:
    print("Escreva sua decisão: ")
    resposta = input()

    if resposta.lower() == 'fim':
        break

    print(conversation({"question": resposta})['text'])
