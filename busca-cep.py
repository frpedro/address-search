import requests

class cep:
    def consultaCep (cep):
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        
        if response.status_code == 200:
            dadosCep = response.json()
            return dadosCep
        else:
            return None

    while True:
        cep = input("Insira seu CEP (Apenas Números): ")
        num = input("Insira o número da casa: ")
        resultadoConsultaCep = consultaCep(cep)
        
        if resultadoConsultaCep:
            
            rua = resultadoConsultaCep.get("logradouro", "Não disponível")
            bairro = resultadoConsultaCep.get("bairro", "Não disponível")
            cidade = resultadoConsultaCep.get("localidade", "Não disponível")
            estado = resultadoConsultaCep.get("estado", "Não disponível")
            cep1 = resultadoConsultaCep.get("cep", "Não disponível")
            
            print(f"Seu produto será entregue na:\nRua: {rua}\nBairro: {bairro}\nNuméro: {num}\nCidade: {cidade}\nEstado: {estado}\nCEP {cep1}")
            break
        else:
            print("Algum erro ocorreu, tente novamente.")
