// etias-connector.js — RMP v3.0
// Proxy via Netlify Function — key nunca expuesta

async function groqCall(messages, model) {
  model = model || "llama-3.3-70b-versatile";
  var res = await fetch("/.netlify/functions/groq", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ model: model, messages: messages, max_tokens: 1000 })
  });
  var data = await res.json();
  return data.choices[0].message.content;
}

async function chatWithETIAS(messages, lang) {
  var system = lang === "pt"
    ? "Você é um agente ETIAS autorizado. Responda em português. Se o usuário quer iniciar o formulário, responda INICIAR_SIMULADOR. Se o caso é complexo, responda ESCALAR_CONSULTOR."
    : lang === "en"
    ? "You are an authorized ETIAS agent. Answer in English. If user wants to start the form, reply INICIAR_SIMULADOR. If complex, reply ESCALAR_CONSULTOR."
    : "Eres un agente ETIAS autorizado. Responde en español. Si el usuario quiere iniciar el formulario, responde INICIAR_SIMULADOR. Si el caso es complejo, responde ESCALAR_CONSULTOR.";
  var groqMessages = [{ role: "system", content: system }].concat(messages);
  return groqCall(groqMessages);
}

async function ocrPassport(base64, mimeType) {
  var prompt = "Extrae los datos de este pasaporte en JSON con estos campos exactos: given_names, surname, date_of_birth (YYYY-MM-DD), nationality, passport_number, expiry_date (YYYY-MM-DD), issuing_country, sex (M o F). Solo JSON, sin explicación.";
  var res = await fetch("/.netlify/functions/groq", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      model: "meta-llama/llama-4-scout-17b-16e-instruct",
      messages: [{
        role: "user",
        content: [
          { type: "image_url", image_url: { url: "data:" + mimeType + ";base64," + base64 } },
          { type: "text", text: prompt }
        ]
      }],
      max_tokens: 500
    })
  });
  var data = await res.json();
  var text = data.choices[0].message.content;
  var clean = text.replace(/```json|```/g, "").trim();
  return JSON.parse(clean);
}

async function ofertaLIC(tvData, lang) {
  var msgs = [{
    role: "system",
    content: "Eres agente de documentación de viaje. El usuario completó su expediente ETIAS. Ofrece la Licencia Internacional de Conducir (LIC) de forma breve y persuasiva. Máximo 3 líneas."
  }, {
    role: "user",
    content: "Destino: " + (tvData.destination || "Europa") + ". Nacionalidad: " + (tvData.nationality || "mexicana") + ". Idioma: " + lang
  }];
  return groqCall(msgs);
}
