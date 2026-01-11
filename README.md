# Dengue, Território e Condições Urbanas no Recife

## 📌 Descrição breve

Este repositório tem o objetivo de transformar dados abertos de saúde pública do Recife, especialmente casos de **Dengue, Zika e Chikungunya** — em **informação acessível, visual e útil**. A partir da análise **territorial e temporal** dos dados, busca-se identificar **padrões**, **desigualdades urbanas** e **áreas prioritárias** que demandam maior atenção do poder público e da sociedade.


## 🎯 Pergunta central

**Por que alguns bairros do Recife sofrem mais com a dengue do que outros, e como as condições urbanas e territoriais influenciam esse risco?**

---

## 🗂️ Fontes de dados

Todos os dados de saúde utilizados neste projeto são provenientes do **Hub de Dados Abertos da Prefeitura do Recife (dados.recife.pe.gov.br)**.

### 📊 Casos de doenças (arquivos CSV)

* **Dengue**: 5 arquivos (anos de 2020 a 2024)
* **Zika**: 5 arquivos (anos de 2020 a 2024)
* **Chikungunya**: 5 arquivos (anos de 2020 a 2024)

Cada arquivo contém registros de casos confirmados, com informações temporais e territoriais.

### 🧭 Tabelas auxiliares

* Tabela de **bairros**
* Tabela de **distritos**
* Tabela de **agravos**
* Tabela de **UF**

### 🧾 Metadados

* 1 arquivo de **metadados em formato JSON**, contendo a descrição das variáveis e informações técnicas dos conjuntos de dados.

O tratamento e a interpretação desse arquivo de metadados fazem parte do escopo do projeto.

---

## 🧱 Pipeline de dados

### 1️⃣ Extração

* Download manual ou automatizado dos arquivos CSV e JSON
* Organização dos dados brutos por tipo de agravo e ano

### 2️⃣ Transformação

* Padronização de colunas e tipos de dados
* Consolidação dos arquivos anuais por agravo
* Tratamento do arquivo de metadados
* Agregação temporal (ano / mês)
* Agregação territorial (bairro)
* Criação de indicadores derivados (ex.: casos por bairro)

> Em etapas futuras, o projeto prevê a incorporação de **dados demográficos e de saneamento** provenientes de outras bases públicas.

### 3️⃣ Carga

* Geração de datasets analíticos finais
* Salvamento de versões intermediárias para rastreabilidade

---

## 📈 Análises previstas

* Evolução temporal dos casos por bairro (2020–2024)
* Comparação espacial entre bairros
* Identificação de áreas com maior recorrência de casos
* Análise comparativa entre Dengue, Zika e Chikungunya
* Mapas temáticos e visualizações interativas
* Modelo preditivo simples (baseline), com fins exploratórios

---

## 🗺️ Uso prático e impacto social

Os resultados deste projeto podem apoiar:

* Planejamento de campanhas de prevenção
* Priorização territorial de ações de saúde
* Alocação de agentes comunitários
* Comunicação clara de dados de saúde para a população

---

## 📁 Estrutura do repositório (proposta)

```text
📦 dengue-recife-territorio-condicoes-urbanas
│
├── data/
│   ├── raw/                # Dados brutos (CSV e JSON)
│   │   ├── dengue/
│   │   ├── zika/
│   │   ├── chikungunya/
│   │   └── metadados/
│   │
│   ├── processed/          # Dados tratados e padronizados
│   └── analytics/          # Datasets analíticos finais
│
├── notebooks/              # Análises exploratórias e estudos
│
├── src/                    # Scripts de ETL e apoio
│   ├── extract/
│   ├── transform/
│   └── load/
│
├── dashboards/             # Arquivos ou links para visualizações
│
├── docs/                   # Documentação e relatórios
│
├── README.md
└── LICENSE
```

---

## 🚧 Status do projeto

🔄 Em desenvolvimento — fase inicial de estruturação, tratamento e exploração dos dados.

---

---

## 📜 Licença

Este projeto utiliza exclusivamente dados públicos e segue os termos de uso definidos pelo Hub de Dados Abertos da Prefeitura do Recife.
