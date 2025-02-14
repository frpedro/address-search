from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Função que consulta o CEP
def consultaCep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        dadosCep = response.json()
        return dadosCep
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        cep = request.form.get("cep")
        num = request.form.get("numero")
        resultadoConsultaCep = consultaCep(cep)
        
        if resultadoConsultaCep:
            rua = resultadoConsultaCep.get("logradouro", "Não disponível")
            bairro = resultadoConsultaCep.get("bairro", "Não disponível")
            cidade = resultadoConsultaCep.get("localidade", "Não disponível")
            estado = resultadoConsultaCep.get("uf", "Não disponível")
            cep1 = resultadoConsultaCep.get("cep", "Não disponível")
            
            return render_template("index.html", 
                                   rua=rua, bairro=bairro, cidade=cidade, 
                                   estado=estado, cep1=cep1, num=num)
        else:
            return render_template("index.html", error="cep não encontrado, tente novamente.")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
