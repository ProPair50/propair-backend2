from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ProPair API (Baby Starter)", version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"ok": True}
async function getProviders() {
  const base = process.env.NEXT_PUBLIC_API_URL!;
  const res = await fetch(`${base}/providers`, { cache: "no-store" });
  return res.json();
}

export default async function ProvidersPage() {
  const providers = await getProviders();

  return (
    <main>
      <h1 style={{ fontSize: "28px", marginBottom: 12 }}>Browse Providers</h1>
      <ul>
        {providers.map((p: any) => (
          <li key={p.id}>
            {p.name} — ⭐ {p.rating}
          </li>
        ))}
      </ul>
    </main>
  );
}
