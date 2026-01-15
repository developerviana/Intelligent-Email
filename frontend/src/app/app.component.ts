import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

type Category = 'Produtivo' | 'Improdutivo';

interface ClassificationResult {
  category: Category;
  suggestion: string;
  confidence?: number;
  source?: string;
  fileName?: string;
}

interface ApiResponse {
  category: Category;
  suggestion: string;
  confidence?: number;
  source?: string;
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'Email Inteligente';
  emailText = '';
  selectedFile: File | null = null;
  fileTextPreview = '';
  loading = false;
  error = '';
  result: ClassificationResult | null = null;
  apiUrl = 'http://localhost:8000/api';
  useMock = true; // desabilite quando o backend estiver disponível

  constructor(private readonly http: HttpClient) {}

  handleFileChange(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (!input.files || input.files.length === 0) {
      return;
    }

    const file = input.files[0];
    this.selectedFile = file;
    this.result = null;
    this.error = '';
    this.fileTextPreview = '';

    if (file.type === 'text/plain') {
      const reader = new FileReader();
      reader.onload = () => {
        this.fileTextPreview = (reader.result as string) || '';
      };
      reader.readAsText(file);
    }
  }

  clearInputs(): void {
    this.emailText = '';
    this.selectedFile = null;
    this.fileTextPreview = '';
    this.result = null;
    this.error = '';
  }

  submit(): void {
    if (!this.emailText.trim() && !this.selectedFile) {
      this.error = 'Envie um arquivo .txt/.pdf ou cole o texto para classificar.';
      return;
    }

    this.loading = true;
    this.error = '';
    this.result = null;

    if (this.useMock) {
      const textSource = this.emailText || this.fileTextPreview || this.selectedFile?.name || '';
      this.result = this.mockClassify(textSource);
      this.loading = false;
      return;
    }

    const formData = new FormData();
    if (this.emailText.trim()) {
      formData.append('text', this.emailText.trim());
    }
    if (this.selectedFile) {
      formData.append('file', this.selectedFile, this.selectedFile.name);
    }

    this.http.post<ApiResponse>(`${this.apiUrl}/classify`, formData).subscribe({
      next: (res) => {
        this.result = {
          category: res.category,
          suggestion: res.suggestion,
          confidence: res.confidence,
          source: res.source || 'API',
          fileName: this.selectedFile?.name
        };
        this.loading = false;
      },
      error: () => {
        const textSource = this.emailText || this.fileTextPreview || this.selectedFile?.name || '';
        this.result = this.mockClassify(textSource);
        this.error = 'API indisponível no momento. Resultado gerado em modo demo.';
        this.loading = false;
      }
    });
  }

  private mockClassify(text: string): ClassificationResult {
    const normalized = text.toLowerCase();
    const isImprodutivo = /feliz|parabéns|obrigado|agradeço|bom dia|boa tarde|boa noite/.test(normalized);
    const isFollowUp = /status|andamento|atualiza|retorno|prazo|protocolo|ticket/.test(normalized);
    const isAttachment = /anexo|arquivo|segue em anexo|pdf|xls|txt/.test(normalized);

    let category: Category = 'Produtivo';
    if (isImprodutivo && !isFollowUp) {
      category = 'Improdutivo';
    }

    const suggestion = category === 'Improdutivo'
      ? 'Agradecer a mensagem de cortesia e informar que não há ação pendente.'
      : isFollowUp
        ? 'Confirmar recepção, informar status atual e, se necessário, fornecer prazo estimado para próxima atualização.'
        : isAttachment
          ? 'Confirmar recebimento do anexo e indicar o próximo passo (ex.: análise técnica ou registro do chamado).'
          : 'Responder com uma confirmação de recebimento e solicitar detalhes adicionais, se faltarem.';

    const confidenceBase = category === 'Produtivo' ? 0.76 : 0.68;

    return {
      category,
      suggestion,
      confidence: confidenceBase,
      source: 'mock-local',
      fileName: this.selectedFile?.name || undefined
    };
  }
}
