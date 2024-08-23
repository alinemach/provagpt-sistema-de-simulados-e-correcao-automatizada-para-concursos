import openai
from config import Config

# Configurar a chave da API do OpenAI
openai.api_key = Config.OPENAI_API_KEY

def correct_text_with_chatgpt(text, instructions):
    try:
        # Fazer uma requisição à API do OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",  # ou outro modelo disponível
            prompt=f"Corrija o seguinte texto de acordo com as regras: {instructions}\n\nTexto:\n{text}",
            max_tokens=1500,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)
