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
        this.error = 'Ocorreu um erro na comunicação com o servidor. Tente novamente mais tarde.';
        this.loading = false;
      }
    });
  }
}