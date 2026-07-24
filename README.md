# Verba AI — Voice Agents for Digital Suvidha

One app, two agents in two languages, plus a live CRM — built for **Digital Suvidha Private
Limited**, the Delhi-based digital marketing and web design agency founded by **Upendra Yadav
("Digital Yadav")**, helping small and medium Indian businesses get online and get found.

| Route | What it shows |
|---|---|
| `/` | Scenario picker → **💬 Consult line** — Simran answers inbound calls about websites, SEO, and social media, diagnoses the caller's situation, and recommends a package · **📅 Consultation invite** — Kritika calls a warm lead and confirms their free 1-on-1 Digital Growth Consultation slot. **Both agents speak English and Hindi** |
| `/crm` | **Verba CRM** — every call's outcome writes back here live (consult enquiries incl. qualified leads/complaints, consultation RSVPs) |

**Stack:** Sarvam Saaras v3 (speech-to-text) · Google Gemini (brain + tools, 80-key hybrid
rotation) · ElevenLabs (voice, auto-falls back to Sarvam Bulbul) · FastAPI + SQLite. No
telephony, no ffmpeg, no Node — the browser captures 16 kHz WAV itself.

Service/pricing data (`services/catalog.py`) is a representative demo dataset built from Digital
Suvidha's real, public service lines — not a scrape of Upendra Yadav's actual direct-client rate
card (none is public; the only published figures found were freelance-marketplace prices, which
are USD and aimed at international clients, not representative of direct-client India pricing).
Confirm real numbers with Digital Suvidha before any production use of this data.

## Setup
```powershell
cd "C:\Users\HP\Claude\Projects\AI service clients\digitalsuvidha-voice-agent"
& "C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe" -m pip install -r requirements.txt

copy .env.example .env      # then open .env and paste your keys
```
Fill `.env`:
- `GEMINI_API_KEY` (+ optional `_2`…`_100` for rotation) — required (aistudio.google.com/apikey)
- `SARVAM_API_KEY` — speech-to-text. Without it the page uses the browser's built-in
  recognition (Chrome/Edge only).
- `ELEVENLABS_API_KEY` + `ELEVENLABS_VOICE_ID` (+ `_HI`) — the voice (English/Hindi).
- `ADMIN_PASSWORD` — kept for compatibility; the page currently has no access gate.

## Run
```powershell
& "C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe" -m uvicorn main:app --reload --port 8012
```
Open **http://localhost:8012** in Chrome/Edge (use `localhost`, not a file:// path — the mic
needs a secure context, which localhost satisfies). Pick a scenario — the **agent speaks
first** (it "picks up").

You can also **type** in the box at the bottom to run without a microphone.

## Architecture notes
- `services/catalog.py` — the service catalog and business-type guide are embedded directly
  into the consult prompt as reference text (static data, not a tool call).
- `services/llm.py` — this build has **zero read/query tools** (unlike the sibling UA Agro
  build's `find_nearest_fap`, a location lookup that doesn't apply here — Digital Suvidha is a
  single Delhi office, not a branch network). Both `log_enquiry` and `log_consultation_rsvp` are
  write-only tools that use the same-turn fast path — no second Gemini call needed to speak the
  confirmation.

## Deploy (Vercel)
```powershell
npx vercel --prod
```
New Vercel projects default Deployment Protection to ON — disable it or the public link
302s to a login page:
```powershell
npx vercel project protection disable digitalsuvidha-voice-agent --sso
```
