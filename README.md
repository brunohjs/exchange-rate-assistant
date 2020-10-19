## Assistente para cotação e conversão monetária
Chatbot de exemplo para iniciantes em RASA. O assistente pode realizar cotações e conversões monetárias. Ele é integrado com uma [API de cotação monetária](https://docs.awesomeapi.com.br/api-de-moedas).



### Organização do projeto
Os arquivos e diretórios do projeto estão organizados da seguinte maneira:

```
    actions/            // Arquivos python com ações customizadas
    data/
        - nlu/          // Intenções e entidades          
        - stories/      // Histórias e fluxos de conversa
    helpers/            // Funções úteis e constantes
    models/             // Arquivos com os modelos treinados de NLU
    scripts/            // Scripts úteis
    services/           // Pasta que contém os serviços de integração
    tests/              // Testes com o assistente
    config.yml          // Configurações do assistente
    credentials.yml     // Credenciais de acesso às plataformas de chat e voice
    domain.yml          // Arquivo que instancia as intenções, entidades e ações do assistente
    endpoints.yml       // Endpoints que o bot pode utilizar
```

### Instruções de instalação
Para executar o chatbot, antes é necessário seguir esses passos:
 1. Instalar o Python (versão 3.6 ou 3.7): [link](https://www.python.org/downloads/);
 
 2. Instalar o RASA: [link](https://rasa.com/docs/rasa/user-guide/installation/);
 
 3. Instalar o RASA-SDK: [link](https://rasa.com/docs/rasa/api/rasa-sdk/#installation);
 
 4. Instalar spaCy (dependência): [link](https://rasa.com/docs/rasa/user-guide/installation/#dependencies-for-spacy)
 
 5. Instalar Docker: [link](https://hub.docker.com/editions/community/docker-ce-desktop-windows/);
 
 6. Instalar o RASA X (opcional): [link](https://rasa.com/docs/rasa-x/installation-and-setup/installation-guide/);
 
 7. Instalar dependências: `pip3 install -r requirements.txt`;

### Instruções de execução
Após seguir as instruções de instalação, seguir essses passos para executar a aplicação:
 - Em um terminal execute o comando `docker run -p 8000:8000 rasa/duckling` para executar o serviço do Duckling (responsável por extrair entidades)
 
 - Em outro terminal execute o comando `rasa run actions` para executar o servidor de ações do RASA;
 
 - Em um terceiro terminal, execute o comando `rasa train && rasa shell` para treinar e testar o bot no terminal.
 - Resumindo, serão 3 serviços rodando em paralelo:
    - Rasa Shell (interface de interação do usuário com o chatbot)
    - Rasa Actions (serviço responsável por fornecer a ação para uma determinada intenção)
    - Duckling (serviço responsável por identificar a entidade de números e valores monetários)
