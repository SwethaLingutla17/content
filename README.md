# AI Content Tool

A minimal end-to-end project that lets you generate marketing and creative content (blog posts, social captions, ads, email promos, product descriptions) using the OpenAI API. Built with **FastAPI** (backend) and **Streamlit** (frontend).

---

## Quick Start

### 1. Clone or download
```bash
git clone <your-fork-url>.git
cd ai-content-tool
```

### 2. Set up Python envs (recommended: separate for backend & frontend)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Backend install & configure
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env  # then edit .env to add your real API key
uvicorn app:app --reload
```

The backend will start at: http://localhost:8000

Test health:
```bash
curl http://localhost:8000/health
```

### 4. Frontend install & run
In another terminal:
```bash
cd ../frontend
pip install -r requirements.txt
streamlit run app_frontend.py
```

By default the frontend points to `http://localhost:8000`. Override by setting `BACKEND_URL` env var.

---

## Configuration

| Variable | Location | Purpose |
|----------|----------|---------|
| `OPENAI_API_KEY` | backend .env or environment | Auth for OpenAI API |
| `OPENAI_MODEL` | backend .env (optional) | Model name (default: gpt-4o-mini) |
| `OPENAI_BASE_URL` | backend .env (optional) | Use a custom endpoint (Azure, proxy, etc.) |
| `BACKEND_URL` | frontend env (optional) | Custom backend URL for Streamlit app |

---

## Prompting Strategy
The backend builds a structured instruction prompt that includes your **content type**, **topic**, **tone**, and optional **word target**, and always reminds the model to keep language clear, engaging, and call-to-action oriented.

You can customize `build_prompt()` in `backend/app.py` to enforce brand voice guidelines, include keywords, add markdown formatting, or embed product data.

---

## Extending the Tool

**Ideas:**
- Add multiple output variants.
- Support image generation (DALL·E, etc.).
- Persist generated outputs to a database (SQLite / Postgres).
- Auto-schedule social posts via Zapier / Make / Meta Graph API.
- Upload sample brand copy and inject style rules into prompts.
- Add user auth & usage logging.

---

## Security Notes
- Never expose your OpenAI API key in frontend code or client-side JavaScript.
- Use environment variables or a secrets manager in production.
- Do not commit your real `.env` file to version control—use `.env.example` as a template.

---

## License
MIT (optional — add LICENSE file if you plan to open source).

---

_Generated on 2025-07-22T00:04:13.423530Z_
