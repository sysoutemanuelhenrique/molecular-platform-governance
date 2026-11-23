# C-1 — Errata de evidência de ambiente

Data: 23/11/2026. Autor: Codex arquiteto. Escopo: inconsistência do estudo v1; documento novo, sem edição do histórico.

## O que está inconsistente

No commit 599a6873b2a55d09c3497780d99794fe337a08e8, study-verification.json registra environment.gemmi_available=true. O estudo v1 afirma que Gemmi não estava instalado. O JSON deriva de uma checagem de descoberta do módulo, não de comprovação de wheel/binding funcional. Esses dois enunciados não podem ser usados como evidência convergente de instalação ou indisponibilidade operacional.

## O que foi reproduzido agora

A pasta externa do script histórico contém uma subpasta gemmi com as fontes oficiais baixadas. Consultando esse diretório por PathFinder.find_spec, foi obtido um spec de namespace com loader=None e origin=None. No contexto neutro da sessão atual, não foi encontrado spec nem distribuição Gemmi registrada.

Isso reproduz uma causa concreta de falso positivo: uma pasta de fontes chamada gemmi pode fazer a descoberta retornar um spec sem que exista o binding científico instalado. A sonda anexa também demonstra o mecanismo numa pasta temporária vazia, independente do checkout ou do ambiente histórico. Não importa Gemmi nem executa suas APIs.

Comando próprio executado nesta reconciliação, fora do código do projeto:

```text
python increments/021/03-study-reconciliation/evidence/probe_namespace_discovery.py
```

O comando foi executado sob o diretório externo desta entrega. A saída está em probe_namespace_discovery.output.json. Não é teste pytest, teste científico, reexecução da sonda C++ do revisor ou validação Windows.

## Correção adotada

- A presença de um spec não comprova que Gemmi estava instalado ou operacional.
- A distribuição/versão funcional histórica de 21/11/2026 permanece não comprovada por essa evidência; não a substituímos por uma medição atual.
- A afirmação documental deve ser: não houve evidência de execução científica ou de binding Gemmi validado pelo estudo v1. O booleano antigo não deve ser usado como prova de instalação funcional.
- O histórico permanece byte-idêntico. Esta errata é a referência de correção; não se muda true para false retroativamente.

Não se infere ausência universal de execução apenas da ausência de uma saída: o registro do estudo declara que não executou Gemmi, e não foi apresentada evidência que contradiga essa declaração. A reconciliação também não executou Gemmi.

ENVIRONMENT CONTRADICTION ACKNOWLEDGED: YES
NAMESPACE FALSE-POSITIVE MECHANISM REPRODUCED: YES
HISTORICAL FUNCTIONAL GEMMI INSTALLATION PROVED: NO
HISTORICAL FILES MODIFIED: NO
SCIENTIFIC ENGINE EXECUTED: NO
