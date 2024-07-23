Feature: Cadastro de produto

  Scenario: Cadastro de produto feito com sucesso
    Given o usuario esteja na pagina de cadastro
    When o usuario entra com dados válidos do produto
    And clica no botao de ENVIAR NOVO PRODUTO
    Then uma confirmacao deve retornar ao usuário e o produto deve ser adicionado a lista de produtos