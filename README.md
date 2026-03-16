Briefing
A coordena ̧c ̃ao do SENAI vem enfrentando dificuldades para acompanhar o desempenho acadˆemico

dos alunos de forma organizada, r ́apida e confi ́avel. Atualmente, as informa ̧c ̃oes de notas che-
gam de maneiras diferentes, com quantidades vari ́aveis de atividades por aluno, o que torna o

processo de an ́alise mais trabalhoso e sujeito a erros.
Um dos principais problemas  ́e que nem sempre os dados recebidos est ̃ao completos ou
corretos. Em alguns casos, a lista de notas de um aluno pode estar vazia, incompleta ou

at ́e corrompida, dificultando a identifica ̧c ̃ao real da sua situa ̧c ̃ao acadˆemica. Isso gera insegu-
ran ̧ca para a coordena ̧c ̃ao e para os professores, que precisam tomar decis ̃oes com base nessas

informa ̧c ̃oes.
Al ́em disso, o processo de verificar aluno por aluno, calcular m ́edias e identificar quem est ́a
em recupera ̧c ̃ao consome tempo e exige aten ̧c ̃ao redobrada. Quando isso  ́e feito manualmente,
aumenta o risco de falhas, atrasos e retrabalho. A coordena ̧c ̃ao precisa de uma forma mais
pr ́atica de percorrer esses dados, processar as notas corretamente e encontrar rapidamente os
casos que exigem aten ̧c ̃ao.

Outro ponto importante  ́e a necessidade de destacar tanto os alunos em situa ̧c ̃ao de re-
cupera ̧c ̃ao quanto aqueles com melhor desempenho. Hoje, essa identifica ̧c ̃ao n ̃ao acontece de

forma autom ́atica, o que dificulta a ̧c ̃oes pedag ́ogicas mais r ́apidas, como apoio aos que tˆem
baixo rendimento e reconhecimento dos alunos com melhor m ́edia.

Tamb ́em existe a necessidade de organizar melhor a solu ̧c ̃ao tecnol ́ogica desenvolvida. A co-
ordena ̧c ̃ao deseja que o sistema seja estruturado de forma modular, separando a execu ̧c ̃ao prin-
cipal do processamento das informa ̧c ̃oes, para facilitar manuten ̧c ̃ao, entendimento e evolu ̧c ̃ao

do c ́odigo. Em outras palavras: n ̃ao basta funcionar, precisa funcionar com organiza ̧c ̃ao —
porque bagun ̧ca em c ́odigo  ́e igual gaveta de cabo: uma hora ningu ́em acha mais nada.

Por fim, h ́a o interesse em gerar um relat ́orio final em arquivo .txt, de forma clara e for-
matada, para que os resultados possam ser consultados, compartilhados e arquivados com

facilidade. Sem isso, a equipe perde tempo procurando informa ̧c ̃oes e n ̃ao consegue ter uma
vis ̃ao consolidada do cen ́ario acadˆemico.












Levantamento de Requisitos
1. Requisitos Funcionais (RF)

O que o sistema deve fazer.

RF01 – Permitir registrar os alunos e suas respectivas notas.

RF02 – Receber listas de notas com quantidade variável de atividades por aluno.

RF03 – Verificar se as listas de notas estão vazias, incompletas ou corrompidas.

RF04 – Calcular automaticamente a média de cada aluno.

RF05 – Identificar alunos que estão em situação de recuperação.

RF06 – Identificar alunos com melhor desempenho acadêmico.

RF07 – Percorrer automaticamente os dados de todos os alunos para análise.

RF08 – Gerar um relatório final com os resultados do processamento.

RF09 – Salvar o relatório em um arquivo .txt.

RF10 – Exibir no relatório informações como nome do aluno, notas, média e situação acadêmica.

2. Requisitos Não-Funcionais (RNF)

São características de qualidade do sistema.

RNF01 – O sistema deve ser desenvolvido em Python.

RNF02 – O código deve ser modular, separando o processamento da execução principal.

RNF03 – O sistema deve possuir tratamento de erros para listas vazias ou dados inválidos.

RNF04 – O sistema deve possuir organização e legibilidade no código.

RNF05 – O processamento dos dados deve ocorrer de forma rápida e automatizada.

RNF06 – O relatório .txt deve ser claro e bem formatado.

RNF07 – O sistema deve permitir manutenção e evolução do código facilmente.

3. Regras de Negócio (RN)

Regras que definem como o sistema toma decisões.

RN01 – A média do aluno deve ser calculada pela soma das notas dividida pela quantidade de atividades.

RN02 – Caso a lista de notas esteja vazia, o sistema deve indicar erro ou dado inválido.

RN03 – Alunos com média abaixo do valor mínimo definido devem ser classificados como em recuperação.

RN04 – Alunos com maiores médias devem ser destacados no relatório.

RN05 – O relatório final deve apresentar a situação acadêmica de cada aluno.

RN06 – O relatório deve ser gerado automaticamente ao final do processamento.