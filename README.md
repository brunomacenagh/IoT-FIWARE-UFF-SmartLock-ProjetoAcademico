# UFF-IoT
Trabalho FInal Disciplina Internet das Coisas - IoT
Universidade Federal Fluminense - UFF - 2023.2
Bruno Macena, Elenice Costa e Rodrigo Oliveira
Projeto "SmartLock"

Sumário do Trabalho:

1. Introdução
2. Objetivos
2.1 Requisitos do sistema
2.2. Escopo do projeto
3. Projeto
3.1 UltraLight 2.0
3.2 Tráfego no sentido sul [Southbound] - Comandos
3.3 Comando Push usando HTTP POST	7
3.4. Tráfego sentido norte [Northbound] - Medições
3.5. Medição usando HTTP GET
3.6. Medição usando HTTP POST
4. Arquitetura	
4.1. Componentes utilizados da Plataforma Fiware	
4.2 Monitor de dispositivos	
5. Aplicação	
5.1. Pré-requisitos:	
5.2 Instalação do ambiente Simulado	
5.3. Instalação e configuração dos Parâmetros VM	
5.4. Instalando Orion via Tutorial:	
6. Teste da Aplicação	
6.1. Abertura da Porta	
6.2. Fechamento da Porta	
6.3. Trancamento da Porta	
7. Documentações de Setup	
7.1. Setup: [Docker-compose.yml]	
7.2. Setup: [Iot Agent Ultralight 2.0]	
7.3. Criando e inicializando os containers e serviços	
7.4 Provisionando uma porta inteligente	
8. Testando IoT Agent via Ultralight 2.0	
8.1. Abrindo a porta inteligente	
8.2. Fechando a porta inteligente	
8.3. Trancando a porta inteligente	
9. Processamento em Python	


Principais Referências

- FIWARE. Installation Guide (Ubuntu 20.04.1). Disponível em: https://github.com/FIWARE/context.Orion-LD/blob/develop/doc/manuals-ld/installation-guide-ubuntu-20.04.1.md. Acesso em: 29 nov. 2023.
- FIWARE. Tutorials: IoT Sensors. Disponível em: https://github.com/fiware/tutorials.iot-sensors. Acesso em: 29 nov. 2023.
Canonical Ltd. Ubuntu 20.04 LTS (Focal Fossa). Disponível em: https://releases.ubuntu.com/20.04/. Acesso em: 29 nov. 2023.
- FIWARE. IoT Agent UL. Disponível em: https://fiware-iotagent-ul.readthedocs.io/. Acesso em: 29 nov. 2023.
- FIWARE. Tutorials: IoT Sensors (GitHub Repository). Disponível em: https://github.com/FIWARE/tutorials.IoT-Sensors.git. Acesso em: 29 nov. 2023.
- Docker, Inc. Install Docker Desktop on Ubuntu. Disponível em: https://docs.docker.com/desktop/install/ubuntu/. Acesso em: 29 nov. 2023.
- Docker, Inc. Install Docker Engine on Ubuntu. Disponível em: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository. Acesso em: 29 nov. 2023.
- FIWARE. IoT Agent. Disponível em: https://fiware-tutorials.readthedocs.io/en/latest/iot-agent.html. Acesso em: 29 nov. 2023.
- HVEX. Segurança Cibernética no Setor Elétrico: Medidores Inteligentes. Disponível em: https://conteudo.hvex.com.br/tecnologia/seguranca-cibernetica-no-setor-eletrico-medidores-inteligentes/. Acesso em: 29 nov. 2023.

1. Introdução:
   
O setor elétrico é um alvo atraente para ataques cibernéticos e acesso indevido, ao ser essencial para o funcionamento da sociedade. As redes de energia elétrica são complexas e interconectadas, o que dificulta proteger contra acessos indevidos (Maia 2023). O setor elétrico brasileiro tem sido alvo de uma série de invasões cibernéticas nos últimos anos. Em 2021, por exemplo, a empresa de energia elétrica Light foi alvo de um ataque que causou uma interrupção no fornecimento de energia para mais de 2 milhões de pessoas no Rio de Janeiro. Segundo Maia (2023) o governo brasileiro tem tomado medidas para melhorar a segurança cibernética do setor elétrico. Em 2021, o governo criou o Centro Nacional de Coordenação de Incidentes Cibernéticos (CNCI), responsável por coordenar a resposta a ataques cibernéticos em infraestruturas críticas, incluindo o setor elétrico.
São medidas de segurança cibernética no setor elétrico, segundo Maia (2023):
Proteção de Infraestrutura crítica: empresas elétricas devem identificar e proteger infraestruturas críticas, como usinas, subestações e sistemas de transmissão, contra ataques cibernéticos ou acesso indevido.
Monitoramento e Detecção: sistemas de monitoramento em tempo real são fundamentais para identificar comportamentos anormais nos sistemas, sinalizando possíveis intrusões ou ameaças.
Segurança de Rede e Comunicação: é crucial proteger as redes de comunicação para evitar acesso não autorizado e interceptação de informações sensíveis.
Gestão de Acesso: controles rigorosos de acesso garantem interações apenas por pessoal autorizado

3. Objetivos:
   
O projeto SmartLock tem como objetivo desenvolver um sistema de controle de acesso autônomo para proteger equipamentos de self-healing em redes elétricas, que pode ser utilizado por distribuidoras para manobras de automação na rede elétrica, que permite retomar o fornecimento de energia em uma área interrompida num curto período.
O SmartLock busca prevenir acessos não autorizados, mitigar riscos de falhas catastróficas e promover a segurança pública. Ele utilizará um sofisticado sensor de alarme combinado com um atuador para controle automatizado de aberturas de porta e um sistema de identificação por RFID, assegurando manutenções seguras e autorizadas. A implementação deste sistema não só eleva a confiabilidade operacional das infraestruturas críticas, mas também estabelece um novo padrão de segurança operacional, contribuindo significativamente para a resiliência das smart cities.

2.1 Requisitos do sistema:

Requisitos Funcionais:
  - Consultar o estado da porta para detectar e responder a acessos não autorizados.
  - Processar informações da tag RFID de identificação para autenticar o acesso dos técnicos.
  - Atuar mecanismos de travamento/destravamento de porta com base na autenticação.
  - Projetar uma interface de usuário para monitoramento operacional, incluindo no mínimo status (open, closed, locked).
  - Estabelecer a comunicação do sistema de controle de acesso com o centro operacional.

Requisitos não Funcionais:
  - Protocolos de Comunicação Padrão - O sistema deve aderir a protocolos de comunicação padrão da indústria para garantir interoperabilidade com diferentes dispositivos e sistemas [HTTPS e REST].
  - Tolerância a Falhas – A abertura de portas deve continuar operando corretamente na presença de falhas de hardware ou software. [Utilização de chave física em situação de contingência]
  - Registro de Atividades - Deve haver repositório que registra as atividades para facilitar a análise de falhas.
  - Tempo de Resposta em milissegundos - O sistema deve ter um tempo de resposta de controle de acesso e sensoriamento. [Pacotes de dados minimalistas]
  - Robustez Contra Falhas - O sistema deve ser robusto contra falhas, com capacidade de manter  operações críticas mesmo em condições de desastres climáticos.
  - Disponibilidade do Sistema - O sistema deve manter alta disponibilidade, minimizando interrupções. [Arquitetura distribuída com contingenciamento].
  - Recuperação Rápida - Em caso de falhas, o sistema deve ser capaz de se recuperar rapidamente.  [Arquitetura com Alta disponibilidade].
  - Capacidade  Expansível - O sistema deve ser projetado para permitir a inclusão fácil de novos componentes.
  - Modularidade - A estrutura do sistema deve ser modular para facilitar ajustes e expansões. [Hardware de baixo custo e compartilhamento de acessos para dados].
  - Padrões de Codificação - O software deve ser desenvolvido seguindo padrões de codificação e boas práticas de mercado para facilitar a manutenção.
  - Documentação - Deve haver uma documentação com Plano do Projeto, Canvas e códigos do software.
  - Modularidade do Código - O código deve ser modular para permitir atualizações e modificações com mínimo esforço e custo.
  - Suporte a diferentes navegadores - O sistema deve funcionar de maneira consistente em vários navegadores web populares. [utilização de sistema – Dashboard em HTML HTTPS].
  - Comunicação Segura - Toda comunicação de dados entre o sistema SmartLock e outros sistemas deve ser realizada de forma segura. [utilização de HTTPS]
  - Interface Intuitiva - A interface do usuário deve ser intuitiva, fácil de navegar e acessível para todos os usuários.
  - Armazenamento de Dados - O sistema deve utilizar mecanismos de armazenamento de dados que sejam adequados para um  ambiente IOT.

2.2. Escopo do projeto:

O projeto SmartLock é implementado na plataforma Fiware tem como escopo proporcionar ao setor de  energia um controle autônomo em infraestrutura críticas de energia. O desenvolvimento da aplicação respeitará as limitações de tempo e orçamento. Portanto, irá se restringir às funcionalidades essenciais e o foco será manter o protótipo limitado às funcionalidades necessárias para validar o conceito, evitando complexidades adicionais. 
Dos requisitos funcionais serão implementados os itens “a, b e c” com a integração da plataforma limitada apenas aos componentes essenciais da plataforma Fiware e testados com dados simulados. O requisito funcional “d” se utilizará da visualização própria do sistema Fiware para monitoramento dos dados. Já o requisito funcional “e” será implementado em momentos futuros uma vez que este projeto se trata da construção de um mínimo produto viável (MVP) e parcerias futuras com mais de um sistema próprio de empresas da rede elétrica possam surgir.
Dos requisitos não funcionais, o foco será nos itens: “a, b, d, j, n e p” que são respectivamente: Protocolos de Comunicação Padrão, Tolerância a Falhas, Tempo de Resposta, Padrões de Codificação, Comunicação Segura e Armazenamento de Dados. Todos foram tratados e definidos a partir das prioridades do projeto com as partes interessadas.

3. Projeto:

O SmartLock é implementado na Plataforma Fiware, com protocolo UltraLight 2.0, utilizando o Orion Context Broker e o Agente IoT. Ele apresenta uma tranca (Porta) inteligente exibido em um navegador e permitindo que o usuário interaja com ela. Uma tranca inteligente é um componente de uma porta eletrônica à qual podem ser enviados comandos para ser trancada ou destravada remotamente. Também pode informar sobre seu estado atual (open, close ou locked). 

3.1 UltraLight 2.0:

É um protocolo leve baseado em texto para dispositivos e comunicações restritas onde a largura de banda e os recursos de memória do dispositivo são limitados. A carga útil para solicitações de medição é uma lista de pares de valores-chave separados pela barra vertical “|”. Por exemplo:

  <chave>|<valor>|<chave>|<valor>|<chave>|<valor>

Por exemplo, uma carga útil como:

  t|15|k|abc

Neste caso, temos dois atributos, um denominado "t" com valor "15" e outro denominado "k" com valor "abc" são transmitidos. Os valores no Ultralight 2.0 são todos tratado como uma string.

3.2 Tráfego no sentido sul [Southbound] - Comandos:

As solicitações HTTP geradas pelo Context Broker e passadas para baixo em direção a um dispositivo IoT (por meio de um Agente IoT) são conhecidas como tráfego sul. O tráfego no sentido sul consiste em comandos dados a dispositivos atuadores que alteram o estado do mundo real por meio de suas ações. Por exemplo, um comando para alterar o estado da tranca inteligente para OPEN abrirá a porta na vida real. Isto, por sua vez, pode alterar as leituras de outros sensores próximos.

3.3 Comando Push usando HTTP POST:

A configuração da comunicação sul entre um Agente IoT e dispositivos IoT é conhecida como provisionamento. Isso garante que o Agente IoT retenha informações suficientes para poder entrar em contato com cada dispositivo IoT. Em outras palavras, ele sabe para onde enviar comandos e quais comandos são suportados. Para enviar um comando a um dispositivo, o Agente IoT envia uma solicitação POST ao endpoint fornecido pelo dispositivo. O corpo da solicitação POST contém o comando.
A carga útil para comandos Ultralight tem o seguinte formato:

  <device_name>@<comand>|<param|<param>

Onde <device_name> é o ID da entidade mantido no intermediário de contexto, <command> é um dos comandos suportados e quaisquer valores adicionais necessários são passados ​​em parâmetros subsequentes, por exemplo:

  urna:ngsi-ld:Door:001@open
Dirá a um dispositivo "Sou conhecido como id="urn:ngsi-ld:Door:001" dentro do Context Broker. Gostaria que o dispositivo escutando neste endpoint executasse o comando open. A resposta Northbound, ou seja, do dispositivo IoT para o Context Broker é a seguinte:

  urna:ngsi-ld:Door:001@Open|Open ok

O que significa "Cumpri uma solicitação da entidade conhecida como id="urn:ngsi-ld:Robot:001" dentro do Context Broker. O comando que executei foi um comando turn. O resultado foi Turn ok".
Como você pode ver, como o comando Southbound define o id usado na interação e os mesmos dados também são retornados, cada resposta sempre pode ser associada à entidade apropriada mantida no Context Broker.
Os comandos push só podem ser usados ​​se o dispositivo for capaz de fornecer um endpoint separado para escutar o tráfego em direção ao sul. Um mecanismo de pesquisa alternativo pode ser usado quando todas as interações são iniciadas no próprio dispositivo, mas isso está além do escopo deste tutorial.

3.4. Tráfego sentido norte [Northbound] - Medições:

As solicitações geradas a partir de um dispositivo IoT e repassadas para o Context Broker (por meio de um agente IoT) são conhecidas como tráfego norte. O tráfego no sentido norte consiste em medições feitas por dispositivos sensores e transmite o estado do mundo real nos dados de contexto do sistema. Por exemplo, uma medição de um sensor de abertura de porta (não comandada) poderia ser retransmitida de volta ao intermediário de contexto para indicar que o estado da mesma mudou sem que tenha havido participação do atuador. Uma assinatura poderia ser feita para ser informado de tais mudanças e provocar outras ações (como ligar um alarme)

3.5. Medição usando HTTP GET:

Um dispositivo pode relatar novas medidas a um Agente IoT usando uma solicitação HTTP GET para um endpoint "conhecido" (o caminho /iot/d) junto com os seguintes parâmetros de consulta:
  i (ID do dispositivo): ID do dispositivo (exclusivo para a chave API).
  k (API Key): Chave API do serviço no qual o dispositivo está registrado.
  t (timestamp): Timestamp da medida. Substituirá o carimbo de data/hora automático do IoTAgent (opcional).
  d (Dados): Carga útil Ultralight 2.0.

É importante citar que os parâmetros i e k são obrigatórios. 
Vamos a um exemplo de solicitação:

  <agente-iot>/iot/d?i= Door:001&d=c|ForcedOpen

Indicaria que o dispositivo id=motion001 deseja informar ao Agente IoT que fez uma medição do mundo real c com o valor ForcedOpen. Isso eventualmente seria repassado ao Context Broker.

3.6. Medição usando HTTP POST:

HTTP POST também pode ser usado. Novamente o caminho será /iot/d, mas neste caso, d (Data) não é necessário - os pares chave-valor da medição são passados ​​como o corpo da solicitação. Os parâmetros de consulta i e k ainda são obrigatórios:
  i (ID do dispositivo): ID do dispositivo (exclusivo para a chave API).
  k (API Key): Chave API do serviço no qual o dispositivo está registrado.
  t (timestamp): Timestamp da medida. Substituirá o carimbo de data/hora automático do IoTAgent (opcional).

4. Arquitetura:
     
O aplicativo de demonstração usará apenas um único componente personalizado que atua como um conjunto de dispositivos IoT. Cada dispositivo IoT usará o protocolo UltraLight 2.0 executado em HTTP. Como todas as interações são iniciadas por solicitações HTTP, as entidades podem ser conteinerizadas e executadas a partir de portas expostas.

4.1. Componentes utilizados da Plataforma Fiware:

Para a base do projeto foram utilizados alguns container’s iniciais: 
-  Projeto FIWARE: FIWARE 201: Introduction to IoT Sensors [tutorials.IoT-Sensors] 
-  Tutorial Principal: https://fiware-iotagent-ul.readthedocs.io/
-  Imagem GIT: https://github.com/FIWARE/tutorials.IoT-Sensors.git

4.2 Monitor de dispositivos:

Para os fins deste trabalho, foram utilizados dois dispositivos IoT fictícios, que eventualmente serão anexados ao Context Broker. O estado de cada dispositivo pode ser visto na página da web do monitor de dispositivos UltraLight, encontrada em: 
-  http://localhost:3000/device/monitor

Nota: Mais informações no documento: RelatorioProjetoSmartLock.pdf > https://github.com/brunomacenagh/IoT-FIWARE-UFF-SmartLock-ProjetoAcademico/blob/main/3.%20RelatorioProjetoSmartLock.pdf

