from inventory_report.inventory.product import Product


def test_cria_produto():
    mock = Product(
        1,
        'ciencia da computacao',
        'trybe',
        '15/08/2022',
        '15/09/2022',
        '16',
        'estudar python'
    )

    assert mock.id == 1
    assert mock.nome_da_empresa == 'trybe'
    assert mock.nome_do_produto == 'ciencia da computacao'
    assert mock.data_de_fabricacao == '15/08/2022'
    assert mock.data_de_validade == '15/09/2022'
    assert mock.numero_de_serie == '16'
    assert mock.instrucoes_de_armazenamento == 'estudar python'
