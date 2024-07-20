Feature: Pesquisa de Produto

  Scenario: Usuário pesquisa por um produto da lista
    Given o usuário estaja na página da lista de produtos
    When o usuário digita o produto procurado na barra de busca
    Then o produto deve ser mostrado no resultado da busca