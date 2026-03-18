import os, datetime

FILES = [
    "AI_CONTEXT/PROYECTO_MASTER.md",
    "AI_CONTEXT/ESTADO_ACTUAL.md",
    "AI_CONTEXT/DECISIONES.md",
    "AI_CONTEXT/FUNDAMENTOS.md",
    "AI_CONTEXT/PROMPTS.md",
]

output = f"# CONTEXTO AUTO-GENERADO — {datetime.date.today()}\n\n"

for f in FILES:
    if os.path.exists(f):
        content = open(f).read()
        output += f"## {f}\n" + content + "\n\n---\n\n"

with open("AI_CONTEXT/PROMPT_CONTEXT.txt", "w") as out:
    out.write(output)

print(f"✅ Contexto generado: {len(output)} chars")
