from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uuid
import webbrowser

from models import IVRRequest
import legacy_ivr
import conversational_ai


# Create FastAPI app
app = FastAPI(
    title="Hospital IVR Modernization - Integration Layer",
    description="Middleware layer connecting Legacy VXML IVR with Conversational AI",
    version="1.0.0"
)

# Enable CORS (allows frontend integration if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory session storage
sessions = {}


# 🔹 Startup Event - Print Docs URL in Terminal
@app.on_event("startup")
def startup_event():
    print("\n")
    print("🚀 Hospital IVR Integration Layer Running Successfully!")
    print("📘 Swagger UI: http://127.0.0.1:8000/docs")
    print("📗 OpenAPI JSON: http://127.0.0.1:8000/openapi.json")
    print("\n")
    # Optional: Auto-open browser
    # webbrowser.open("http://127.0.0.1:8000/docs")


# 🔹 Health Check Endpoint
@app.get("/")
def health_check():
    return {"status": "Integration Layer Running Successfully"}


# 🔹 Start IVR Call (Session Creation)
@app.post("/ivr/start")
def start_call():
    session_id = str(uuid.uuid4())
    sessions[session_id] = {"current_menu": "main"}

    menu = legacy_ivr.get_menu("main")

    return {
        "session_id": session_id,
        "source": "legacy_vxml",
        "prompt": menu["prompt"]
    }


# 🔹 Handle IVR Input (Core Integration Logic)
@app.post("/ivr/input")
def handle_input(request: IVRRequest):
    session = sessions.get(request.session_id)

    if not session:
        return {"error": "Invalid session"}

    current_menu = session["current_menu"]
    menu = legacy_ivr.get_menu(current_menu)

    # 1️⃣ Traditional DTMF Flow (Legacy VXML)
    if request.user_input.isdigit():

        if request.user_input in menu["options"]:
            next_menu = menu["options"][request.user_input]
            session["current_menu"] = next_menu

            next_menu_data = legacy_ivr.get_menu(next_menu)

            if next_menu_data:
                return {
                    "source": "legacy_vxml",
                    "prompt": next_menu_data["prompt"]
                }
            else:
                return {
                    "source": "legacy_vxml",
                    "prompt": "Operation completed successfully."
                }

        else:
            return {
                "source": "legacy_vxml",
                "prompt": "Invalid option. Please try again."
            }

    # 2️⃣ Conversational AI Flow (Modernized IVR)
    else:
        ai_response = conversational_ai.process_natural_language(request.user_input)

        return {
            "source": "conversational_ai",
            "intent": ai_response["intent"],
            "prompt": ai_response["response_text"]
        }