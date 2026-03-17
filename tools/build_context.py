import os, datetime

FILES = [
    "AI_CONTEXT/PROYECTO_MASTER.md",
    "AI_CONTEXT/ESTADO_ACTUAL.md",
    "AI_CONTEXT/DECISIONES.md",
    "AI_CONTEXT/FUNDAMENTOS.md",
]

output = f"# CONTEXTO AUTO-GENERADO — {datetime.date.today()}\n\n"

for f in FILES:
    if os.path.exists(f):
        content = open(f).read()
        lines = content.split('\n')[:300]
        output += f"## {f}\n" + '\n'.join(lines) + "\n\n---\n\n"

with open("AI_CONTEXT/PROMPT_CONTEXT.txt", "w") as out:
    out.write(output)

chars = len(output)
print(f"✅ Contexto generado: {chars} chars (~{chars//4} tokens)")
print("📋 Archivo listo: AI_CONTEXT/PROMPT_CONTEXT.txt")
