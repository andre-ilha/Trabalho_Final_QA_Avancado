Feature: Login e Logout de Usuario

  Scenario: Login efetuado com sucesso
    Given o usuario esteja na pagina de login
    When o usuario entra com e-mail e senha válidos
    And clica no botao de login
    Then o usuario deve ser redirecionado ao seu dashboard