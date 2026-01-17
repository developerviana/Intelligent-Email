# Email Inteligente - Frontend

Interface moderna e responsiva desenvolvida em **Angular 17** para interação com a API de classificação de e-mails.

## 🎨 Funcionalidades e Design

-   **Dashboard Otimizado**: Layout de "visão única" (viewport fit) responsivo para qualquer tamanho de tela.
-   **Design System**: Background com textura "Dot-Grid", cartões flutuantes e tipografia limpa.
-   **Interatividade**:
    -   Drag & Drop para upload de arquivos.
    -   Inputs dinâmicos para texto direto.
    -   Feedback visual de carregamento e erros.
-   **Integração**: Conectado via `HttpClient` ao backend FastAPI.

## 🛠️ Stack Tecnológica

-   **Angular 17** (Standalone Components - sem NgModules).
-   **SCSS**: Uso avançado de mixins e CSS Variables.
-   **TypeScript**: Tipagem estrita para interfaces de API.

## 🚀 Como Rodar Localmente

1.  **Instale as dependências:**
    ```bash
    npm install
    ```

2.  **Inicie o servidor de desenvolvimento:**
    ```bash
    ng serve
    ```
    Acesse em: `http://localhost:4200`

## 📦 Deploy (Vercel)

Este projeto contém configuração específica para deploy na Vercel:
-   `vercel.json`: Gerencia o roteamento de SPA (Single Page Application).
-   `angular.json`: Configurações de build otimizadas ("budget" ajustado).

O comando de build utilizado é:
```bash
ng build
```
Os artefatos são gerados em: `dist/frontend/browser`

