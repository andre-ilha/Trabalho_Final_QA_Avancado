Feature: Cadastro de Usuário

  Scenario: Cadastro de usuário efetuado com sucesso
    Given o usuario esteja na página de registro
    When ele preenche os dados com informações válidas
    And clica em criar conta
    Then uma confirmacao deve retornar ao usuario e retorna a página principal para login
