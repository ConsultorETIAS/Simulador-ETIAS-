import os, datetime

FILES = [
    "AI_CONTEXT/PROYECTO_MASTER.md",
    "AI_CONTEXT/ESTADO_ACTUAL.md",
    "AI_CONTEXT/DECISIONES.md",
    "AI_CONTEXT/FUNDAMENTOS.md",
    "AI_CONTEXT/PROMPTS.md",
]

today = datetime.date.today().isoformat()

# Solo actualiza la línea "Fecha:" al inicio, no todas las fechas
import re
estado_path = "AI_CONTEXT/ESTADO_ACTUAL.md"
if os.path.exists(estado_path):
    content = open(estado_path).read()
    content = re.sub(r'(?m)^(\*\*Fecha\*\*: )\d{4}-\d{2}-\d{2}', f'\\g<1>{today}', content)
    open(estado_path, "w").write(content)

output = f"# CONTEXTO AUTO-GENERADO — {today}\n\n"

for f in FILES:
    if os.path.exists(f):
        content = open(f).read()
        output += f"## {f}\n" + content + "\n\n---\n\n"

with open("AI_CONTEXT/PROMPT_CONTEXT.txt", "w") as out:
    out.write(output)

print(f"✅ Contexto generado: {len(output)} chars")
