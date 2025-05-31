from agno.tools.base import Tool
from openai import OpenAI

class PHPHelperTool(Tool):
    def run(self, input_text: str) -> str:
        prompt = f"""
Você é um desenvolvedor PHP experiente. Sua missão é ajudar a gerar, revisar e explicar códigos PHP legados.
Entrada do usuário:
{input_text}
Responda de forma direta, com código quando necessário.
"""
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
