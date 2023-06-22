import sys
import openai
import requests
import json


if __name__=="__main__":
        debug=True
        openai.api_key_path = "./ccrt"
        model="gpt-3.5-turbo"
        role="user"
        prompt=""
        if (debug):  print(f"Arguments count: {len(sys.argv)}")
        for i, args in enumerate(sys.argv):
                if i > 0 and i < len(sys.argv):
                        prompt+=sys.argv[i]+" "
                i = i + 1
        try :
                if (debug):  print ("Pregunta:\n"+ prompt)
                response = openai.ChatCompletion.create(model=model,
                                                messages=[{"role":role,
                                                        "content":prompt}])

        # Obteniendo solo el contenido
                content=response['choices'][0]['message']['content']

                print ("Respuesta:\n"+ content)

        except IndexError:
                print("An error has occurred:")
                print ("Prompt: " + prompt)
