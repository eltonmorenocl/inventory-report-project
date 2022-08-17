from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(products):
        simple_report = SimpleReport.generate(products)

        nome_empresa = [p["nome_da_empresa"] for p in products]

        produtos_string = 'Produtos estocados por empresa:\n'

        qnt_empresas = {
            empresa: nome_empresa.count(empresa) for empresa in nome_empresa
        }

        empresas_list = ""
        for empresa, qnt in qnt_empresas.items():
            empresas_list += f"- {empresa}: {qnt}\n"

        return (
            f"{simple_report}\n"
            f"{produtos_string}"
            f"{empresas_list }"
        )
