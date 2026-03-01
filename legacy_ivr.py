"""
Simulated Legacy VXML-based IVR System
"""

MENUS = {
    "main": {
        "prompt": "Welcome to City Hospital. Press 1 for Appointments, 2 for Lab Reports, 3 for Emergency.",
        "options": {
            "1": "appointments",
            "2": "lab_reports",
            "3": "emergency"
        }
    },
    "appointments": {
        "prompt": "Press 1 to book appointment. Press 2 to cancel appointment.",
        "options": {
            "1": "book_appointment",
            "2": "cancel_appointment"
        }
    },
    "lab_reports": {
        "prompt": "Enter your patient ID followed by #.",
        "options": {}
    }
}

def get_menu(menu_name: str):
    return MENUS.get(menu_name)