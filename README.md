# Workshop: Chatbot LLM

## Persiapan Awal (Setup)

**1. Buat Virtual Environment & Aktifkan**

```bash
python -m venv venv

# Pengguna Windows:
venv\Scripts\activate
# Pengguna Mac/Linux:
source venv/bin/activate
```

**2. Install Dependensi (Library)**

```bash
pip install -r requirements.txt
```

**3. Setup API Key**

Copy file environment:

```bash
cp .env.example .env
```

Untuk Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

- Buka file `.env` tersebut dan masukkan API Key Gemini(didapatkan dari [Google AI Studio](https://aistudio.google.com/)).

---

## Cara Menjalankan Aplikasi

Aplikasi ini dibangun menggunakan **FastAPI**. Untuk menyalakan server lokal, jalankan perintah ini di terminal:

```bash
uvicorn main:app --reload
```

Setelah server menyala, buka **[http://localhost:8000/docs](http://localhost:8000/docs)** di _browser_ untuk membuka Swagger.

---

## Struktur Folder

- `main.py` : Endpoint API tempat kita menerima dan membalas _chat_.
- `service.py` : File utama tempat untuk menyusun logika LLM, RAG, dan Agent. Ikuti komentar `TODO` di dalamnya.
- `schemas.py` : Struktur data Pydantic.
- `data/` : Folder berisi dokumen internal kafe (_knowledge base_) untuk keperluan fitur RAG.

## Daftar Tugas

### 1. Bikin Tool Baru

**Instruksi:**
Buat satu fungsi (_tool_) baru dengan nama `cek_harga_menu`. Fungsi ini tugasnya nyari harga dari sebuah _dictionary_ sederhana (harganya bebas karang aja, misal: `kopi susu aren = 15000`). Terus, jangan lupa daftarin _tool_ itu ke dalam _list tools_.

- **Contoh pertanyaan:** _"Harga kopi susu aren berapa?"_
- **Output yang diharapkan:** AI bisa jawab informasi harga setiap menu dengan bener.

<img width="960" height="540" alt="Screenshot 2026-07-24 231528" src="https://github.com/user-attachments/assets/d4a8cee3-6d66-4601-979b-368505825998" />

### 2. Modifikasi Knowledge RAG

**Instruksi:**
Tambahin 1 dokumen baru yang isinya info operasional kafe biar AI-nya makin pintar. Habis itu, jalanin proses _ingest_ data biar _database vector_-nya ke-update.

- **Contoh pertanyaan:** _"Kafe ini buka dari jam berapa?"_
- **Output yang diharapkan:** AI bisa ngejelasin jam buka/tutup kafe pakai data baru yang udah ditambahin.

<img width="960" height="540" alt="Screenshot 2026-07-24 231609" src="https://github.com/user-attachments/assets/11169776-09aa-4d22-9c4e-c5d41014e88b" />


### 3. Guardrails (Scope Limitation) & Persona

**Instruksi:**
Modif _system prompt_-nya ya. Tambahin instruksi (_guardrails_) berupa _Scope Limitation_ dan _Persona_ supaya AI-nya:

1. Selalu jawab pakai gaya bahasa pelayan kafe yang asyik/gaul (misal pakai lo/gue atau sapaan khas).
2. Nolak tegas kalau ditanya hal-hal di luar urusan kafe atau menu (misal: urusan politik, sejarah, rekomendasi film, dll).

- **Contoh pertanyaan:** _"Eh bro, gue mau tanya kebijakan pemerintah sekarang gimana sih?"_
- **Output yang diharapkan:** AI jawabnya tetap asyik, tapi nolak buat bahas topik itu dan langsung ngarahin pembicaraan balik ke pesanan kafe.

<img width="960" height="540" alt="Screenshot 2026-07-24 231416" src="https://github.com/user-attachments/assets/dd7251d9-14ee-409a-b536-a66cd6eba445" />

---

## Catatan Pengumpulan

1. **Pengerjaan Kuis:** Kerjakan soal sesuai dengan panduan diatas.
2. **Testing di Swagger:** Setelah itu lakukan testing di swagger, lalu untuk input dan outputnya di screenshot.
3. **Update README:** Taruh screenshot tadi persis di bawah poin masing-masing soal di file `README.md`.
4. **Push & Submit:** _Commit_ dan _push_ hasil pengerjaan ke GitHub masing-masing. Lalu kirimkan link github masing masing ke dalam form pengumpulan tugas yang sudah disiapkan. https://forms.gle/FAuAn7xrmV4dQLDZ6
