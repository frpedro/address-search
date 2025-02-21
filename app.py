from flask import Flask, render_template, request
import requests

# Inicializa a aplicação Flask
app = Flask(__name__)

# Função que consulta o CEP usando a API ViaCEP
def consulta_cep(cep):
    
    # Monta a URL da API ViaCEP com o CEP fornecido
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    # Realiza a requisição
    response = requests.get(url)
    
    # Se a requisição for bem sucedida, retorna os dados do CEP em formato JSON
    if response.status_code == 200:
        dados_cep = response.json()
        return dados_cep
    
    # Se a requisição falhar, não retorna nada
    else:
        return None


# Função que lida com o recebimento do formulário e exibe os resultados
@app.route("/", methods=["GET", "POST"])
def index():
    
    if request.method == "POST": 
        
        # Obtém os dados enviados pelo formulário
        cep = request.form.get("cep")
        num = request.form.get("numero")
        
        # Realiza a consulta
        resultado_consulta_cep = consulta_cep(cep)
        
        # Se a consulta for bem-sucedida, exibe os dados encontrados (E os não encontrados com "Não disponível")
        if resultado_consulta_cep:
            rua = resultado_consulta_cep.get("logradouro", "Não disponível")
            bairro = resultado_consulta_cep.get("bairro", "Não disponível")
            cidade = resultado_consulta_cep.get("localidade", "Não disponível")
            estado = resultado_consulta_cep.get("uf", "Não disponível")
            cep1 = resultado_consulta_cep.get("cep", "Não disponível")
            
            # Retorna a página com os dados do endereço
            return render_template("index.html", 
                                   rua=rua, bairro=bairro, cidade=cidade, 
                                   estado=estado, cep1=cep1, num=num)
            
        # Se não encontrar os dados do CEP, exibe uma mensagem de erro
        else:
            return render_template("index.html", error="cep não encontrado, tente novamente.")
    
    # Renderiza o formulário vazio.
    # Necessário para que a página rode corretamente.
    return render_template("index.html")

# Roda a aplicação
if __name__ == "__main__":
    app.run(debug=True)
