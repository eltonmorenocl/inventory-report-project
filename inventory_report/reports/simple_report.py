from datetime import date


class SimpleReport:
    @staticmethod
    def generate(list):

        data_fabricacao = min([data["data_de_fabricacao"] for data in list])

        data_validade = min([data["data_de_validade"] for data in list
                            if data['data_de_validade']
                            >= str(date.today())])

        nome_empresa = [p["nome_da_empresa"] for p in list]

        empresa_qtd_produtos = max(set(nome_empresa), key=nome_empresa.count)

        return (
          f"Data de fabricação mais antiga: {data_fabricacao}\n"
          f"Data de validade mais próxima: {data_validade}\n"
          f"Empresa com mais produtos: {empresa_qtd_produtos}"
        )
