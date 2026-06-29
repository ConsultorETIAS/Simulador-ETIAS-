#!/data/data/com.termux/files/usr/bin/bash
set -e

read -p "Ruta al archivo JSON de la Service Account: " SA_FILE
read -p "Tu issuerId (Wallet Business Console): " ISSUER_ID

if [ ! -f "$SA_FILE" ]; then
  echo "❌ No se encontró el archivo: $SA_FILE"
  exit 1
fi

echo ""
echo "🔑 Generando token OAuth y creando la clase..."

python3 << PYEOF
import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

SA_FILE = "$SA_FILE"
ISSUER_ID = "$ISSUER_ID"
CLASS_ID = f"{ISSUER_ID}.etias_representante"

SCOPES = ["https://www.googleapis.com/auth/wallet_object.issuer"]

creds = service_account.Credentials.from_service_account_file(SA_FILE, scopes=SCOPES)
creds.refresh(Request())
token = creds.token

generic_class = {
    "id": CLASS_ID,
    "issuerName": "ETIAS Pass - Daniel Gómez Gamiño",
    "classTemplateInfo": {
        "cardTemplateOverride": {
            "cardRowTemplateInfos": [
                {
                    "twoItems": {
                        "startItem": {
                            "firstValue": {
                                "fields": [{"fieldPath": "object.textModulesData['expediente']"}]
                            }
                        },
                        "endItem": {
                            "firstValue": {
                                "fields": [{"fieldPath": "object.textModulesData['fecha']"}]
                            }
                        }
                    }
                }
            ]
        }
    }
}

url = f"https://walletobjects.googleapis.com/walletobjects/v1/genericClass/{CLASS_ID}"
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

r = requests.get(url, headers=headers)
if r.status_code == 200:
    print(f"✅ La clase '{CLASS_ID}' ya existe. No es necesario crearla de nuevo.")
else:
    create_url = "https://walletobjects.googleapis.com/walletobjects/v1/genericClass"
    r = requests.post(create_url, headers=headers, json=generic_class)
    if r.status_code in (200, 201):
        print(f"✅ Clase creada exitosamente: {CLASS_ID}")
    else:
        print(f"⚠️  Respuesta inesperada ({r.status_code}):")
        print(r.text)
PYEOF
