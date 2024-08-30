import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("API_KEY"))


def get_car_ai_description(brand, model, year):
    message = f""" 
    Me mostre uma descrição de venda para o carro {brand} {model} {year} mas em apenas 200 caracteres. 
    Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro. 
    Trazer apenas dados concretos para amostra do usuário, sem outras interações com banco de dados
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(message)
    return response.text
