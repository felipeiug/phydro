# Guia de contribuição

Obrigado por querer contribuir com o projeto `phydro`.

Este documento define o padrão esperado para branches, commits e pull requests, para manter o projeto organizado e fácil de revisar.

## 1. Fluxo recomendado

1. Faça um fork do repositório ou use uma branch local a partir da branch principal.
2. Crie uma branch com o objetivo da mudança.
3. Faça alterações pequenas e focadas.
4. Execute a validação relevante do projeto.
5. Abra um PR com descrição clara e checklist.
6. Responda aos comentários e ajuste o que for pedido.

## 2. Convenção de branches

Use nomes curtos e descritivos:

- `feature/nome-da-funcionalidade`
- `fix/corrige-bug-em-x`
- `docs/atualiza-readme`
- `refactor/ajusta-formatacao`
- `chore/atualiza-dependencias`

Evite nomes genéricos como `update`, `teste` ou `final`.

## 3. Mensagens de commit

Prefira commits curtos e objetivos, com mensagens em português ou em inglês seguindo o padrão:

- `feat: adiciona suporte a ...`
- `fix: corrige erro em ...`
- `docs: atualiza documentação de ...`
- `refactor: reorganiza ...`
- `chore: atualiza dependências`

Se a mudança for pequena e focada, um commit por alteração é melhor do que vários commits misturados.

## 4. Regras antes de abrir um PR

Antes de enviar o PR, confirme:

- [ ] a branch foi criada a partir da branch principal atualizada;
- [ ] a alteração é específica e está bem descrita;
- [ ] o código foi executado localmente;
- [ ] os testes relevantes foram executados, se existirem;
- [ ] a documentação foi atualizada quando necessário;
- [ ] não há arquivos temporários ou trechos de debug esquecidos;
- [ ] o PR não mistura correções, documentação e refatorações sem necessidade.

## 5. Padrão de Pull Request

Ao abrir um PR, siga este formato:

### Título

Use um título curto e objetivo:

- `feat: adiciona função para ...`
- `fix: corrige erro ao consultar ...`
- `docs: melhora guia de contribuição`

### Descrição

Inclua:

- resumo da mudança;
- problema que motivou a alteração;
- o que foi alterado;
- como validar localmente;
- links ou referências relevantes, se houver.

### Checklist do PR

- [ ] Descrevi claramente o objetivo da mudança
- [ ] A funcionalidade ou correção foi testada localmente
- [ ] Atualizei a documentação quando necessário
- [ ] O código está consistente com o padrão do projeto
- [ ] Não deixei arquivos temporários ou debug no código

## 6. Exemplo de PR

### Título
`fix: corrige leitura de arquivos de estação`

### Corpo

```md
## Resumo
Corrige a forma como os arquivos de estação são lidos durante a extração dos dados.

## O que mudou
- ajusta a normalização dos nomes dos arquivos;
- evita falha quando a estação não possui um tipo esperado;
- melhora a descrição do erro em casos de ausência de dados.

## Validação
- executei a função localmente com uma estação real;
- confirmei que os dados são retornados no formato esperado.

## Checklist
- [x] Descrevi objetivo da mudança
- [x] Testei localmente
- [x] Atualizei a documentação
- [x] Revisei o diff antes de abrir o PR
```

## 7. Dicas finais

- PRs pequenos e bem focados são mais fáceis de revisar.
- Uma mudança clara com boa descrição reduz retrabalho.
- Se a dúvida for grande, abra uma issue antes ou comente no PR.

Obrigado pela contribuição!
