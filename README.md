# 🔐 Teste de Senhas em Arquivo ZIP

## 📌 Descrição

Este projeto é um script em Python que tenta abrir um arquivo `.zip` protegido por senha, utilizando uma lista pré-definida de possíveis senhas.

O objetivo é demonstrar o funcionamento da biblioteca `zipfile` e como arquivos compactados protegidos por senha podem ser testados de forma automatizada.

---

## ⚙️ Tecnologias Utilizadas

* Python 3
* Biblioteca padrão `zipfile`

---

## 🧠 Como o Script Funciona

O algoritmo segue o seguinte fluxo:

### 1. 📁 Abre o arquivo ZIP

O script acessa o arquivo compactado informado no caminho:

```python id="zip01"
zip_path = "arquivo.zip"
```

---

### 2. 🔑 Lista de senhas

Uma lista de possíveis senhas é definida manualmente:

```python id="zip02"
senhas_para_testar = ["luiz", "lampreia", "luiz123", ...]
```

Essas senhas são testadas uma por uma.

---

### 3. 🔁 Tentativa de extração

Para cada senha da lista:

* O script tenta abrir o ZIP
* Se a senha estiver correta → arquivos são extraídos
* Se estiver errada → erro é ignorado e o próximo teste continua

---

### 4. ✅ Senha encontrada

Se uma senha funcionar:

* O script exibe a senha correta
* Interrompe a execução imediatamente

---

### 5. ❌ Nenhuma senha válida

Se nenhuma senha funcionar:

* O script informa que nenhuma senha da lista foi válida

---

## 🧾 Código principal (resumo)

```python id="zip03"
with zipfile.ZipFile(zip_path) as z:
    for senha in senhas_para_testar:
        try:
            print(f"Testando: {senha}")
            z.extractall(pwd=senha.encode())
            print(f"SENHA ENCONTRADA: {senha}")
            break
        except:
            pass
```

---

## 🚀 Como Executar

### 1. Coloque o arquivo ZIP na pasta do projeto

Exemplo:

```
arquivo.zip
```

---

### 2. Execute o script

```bash id="zip04"
python script.py
```

---

## 📊 Resultado esperado

### ✔ Caso sucesso:

```
Testando: luiz123
SENHA ENCONTRADA: luiz123
```

### ❌ Caso falha:

```
Nenhuma das senhas da lista funcionou.
```

---

## ⚠️ Aviso de Uso Responsável

Este projeto tem finalidade **educacional**, demonstrando o funcionamento de arquivos ZIP protegidos por senha.

O uso deste código para:

* acessar arquivos sem permissão
* tentar quebrar senhas de terceiros
* ou qualquer atividade ilegal

**é proibido e pode violar leis de segurança digital.**

O autor não se responsabiliza pelo uso indevido deste código.

---

## 🔐 Limitações do Método

* Funciona apenas com senhas da lista
* Não realiza quebra de senha real (força bruta completa)
* Pode ser lento se a lista for grande
* Arquivos ZIP podem ter criptografia forte

---

## 💡 Possíveis Melhorias

* Leitura de senhas via arquivo `.txt`
* Paralelização das tentativas
* Interface gráfica simples
* Registro de logs em arquivo
* Integração com dicionários maiores

---

## 👨‍💻 Objetivo do Projeto

* Entender como funciona proteção de arquivos ZIP
* Praticar automação em Python
* Simular ataque por dicionário (conceito teórico de segurança)

---
