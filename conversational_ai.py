"""
Simulated Conversational AI Engine (ACS/BAP Mock)
"""

def process_natural_language(text: str):
    text = text.lower()

    if "book" in text:
        return {
            "intent": "book_appointment",
            "response_text": "Sure, I can help you book an appointment. Please provide preferred date."
        }

    elif "cancel" in text:
        return {
            "intent": "cancel_appointment",
            "response_text": "Your appointment cancellation request is being processed."
        }

    elif "report" in text:
        return {
            "intent": "lab_reports",
            "response_text": "Please provide your patient ID to retrieve lab reports."
        }

    elif "emergency" in text:
        return {
            "intent": "emergency",
            "response_text": "Connecting you immediately to emergency services."
        }

    else:
        return {
            "intent": "unknown",
            "response_text": "Sorry, I did not understand. Please try again."
        }