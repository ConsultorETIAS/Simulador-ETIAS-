exports.handler = async function(event, context) {
  console.log("Function invoked. Method:", event.httpMethod);
  
  if (event.httpMethod !== "POST") {
    return {
      statusCode: 405,
      headers: {"Access-Control-Allow-Origin": "*"},
      body: JSON.stringify({error: "Method not allowed"})
    };
  }

  try {
    if (!event.body) {
      console.error("Missing request body");
      return {
        statusCode: 400,
        headers: {"Access-Control-Allow-Origin": "*"},
        body: JSON.stringify({error: "Missing request body"})
      };
    }

    const body = JSON.parse(event.body);
    console.log("Request to Groq with model:", body.model || "default");
    
    if (!process.env.GROQ_API_KEY) {
      console.error("GROQ_API_KEY not set in environment");
      return {
        statusCode: 500,
        headers: {"Access-Control-Allow-Origin": "*"},
        body: JSON.stringify({error: "API key not configured. Please set GROQ_API_KEY in Netlify environment variables."})
      };
    }

    const groqResponse = await fetch("https://api.groq.com/openai/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + process.env.GROQ_API_KEY
      },
      body: JSON.stringify(body)
    });

    const data = await groqResponse.json();
    console.log("Groq response status:", groqResponse.status);
    
    // Detectar específicamente error de API key
    if (groqResponse.status === 401 || (data.error && data.error.code === "invalid_api_key")) {
      console.error("Invalid API key detected");
      return {
        statusCode: 401,
        headers: {"Access-Control-Allow-Origin": "*"},
        body: JSON.stringify({error: "Invalid Groq API key. Please check your environment variables."})
      };
    }
    
    return {
      statusCode: groqResponse.status,
      headers: {"Access-Control-Allow-Origin": "*"},
      body: JSON.stringify(data)
    };
    
  } catch (error) {
    console.error("Function error:", error);
    return {
      statusCode: 500,
      headers: {"Access-Control-Allow-Origin": "*"},
      body: JSON.stringify({error: error.message || "Internal server error"})
    };
  }
};
