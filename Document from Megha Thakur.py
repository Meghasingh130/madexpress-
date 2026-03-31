import pyttsx3
import webbrowser

# Initialize Text-to-Speech
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print("MadExpress:", text)
    engine.say(text)
    engine.runAndWait()

def suggest_medicine(condition):
    # Medicine database with name, details, and purchase links (PharmEasy)
    medicines = {
        "headache": {
            "name": "Paracetamol 650mg Tablet",
            "details": "Used to relieve pain and reduce fever. Take one tablet every 6 to 8 hours after meals if required.",
            "link": "https://blinkit.com/prn/dolo-650mg-strip-of-15-tablets/prid/639498?srsltid=AfmBOoo85kpxQYwlVMFY_8xz3wzdriCDKXmao9UuC1tbsc1-7Jc8bTNF"
        },
        "cold": {
            "name": "Cetirizine 10mg Tablet",
            "details": "Helps reduce sneezing, runny nose, and watery eyes caused by cold or allergies. Take one tablet daily at night.",
            "link": "https://blinkit.com/s/?q=Cetirizine"
        },
        "fever": {
            "name": "Crocin Advance Tablet",
            "details": "Effective in reducing fever and mild pain. Take one tablet after food when fever occurs.",
            "link": "https://blinkit.com/prn/crocin-advance-500mg-strip-of-20-tablets/prid/639510"
        },
        "cough": {
            "name": "Benadryl Cough Syrup",
            "details": "Relieves cough and throat irritation. Take 2 teaspoons twice a day after meals.",
            "link": "https://blinkit.com/prn/honitus-cough-syrup/prid/988"
        },
        "stomach pain": {
            "name": "Drotin DS Tablet",
            "details": "Used to relieve abdominal cramps and stomach pain. Take one tablet twice a day after meals.",
            "link": "https://blinkit.com/prn/drotin-ds-80mg-strip-of-15-tablets/prid/647416"
        },
        "acidity": {
            "name": "Digene Tablet",
            "details": "Provides quick relief from acidity, gas, and heartburn. Chew one tablet after meals.",
            "link": "https://blinkit.com/prn/disprin-regular-325mg-strip-of-10-effervescent-tablets/prid/650511"
        },
        "sore throat": {
            "name": "Strepsils Lozenges",
            "details": "Soothes sore throat and throat pain. Dissolve one lozenge slowly in the mouth every 2–3 hours.",
            "link": "https://blinkit.com/prn/himalaya-koflet-cough-lozenges/prid/439060"
        },
        "body pain": {
            "name": "Brufen 400mg Tablet",
            "details": "Used for mild to moderate body pain and inflammation. Take one tablet after meals if needed.",
            "link": "https://blinkit.com/prn/brufen-400mg-strip-of-20-tablets/prid/643637"
        },
        "vomiting": {
            "name": "Domstal 10mg Tablet",
            "details": "Prevents nausea and vomiting. Take one tablet before meals, twice a day if required.",
            "link": "https://blinkit.com/prn/domstal-10mg-strip-of-10-tablets/prid/644481"
        },
        "loose motion": {
            "name": "Eldoper Capsul",
            "details": "Used to control diarrhea and loose motion. Take one capsule after each loose motion, up to 3 times a day.",
            "link": "https://pharmeasy.in/online-medicine-order/eldoper-capsule-15777"
        }
    }

    condition = condition.lower()

    if condition in medicines:
        med = medicines[condition]
        med_name = med["name"]
        med_details = med["details"]
        med_link = med["link"]

        # Speak and print medicine info
        speak(f"For {condition}, I recommend {med_name}.")
        speak(med_details)

        print(f"\n💊 Medicine Name: {med_name}")
        print(f"📄 Details: {med_details}")

        # Ask user if they want to buy
        speak("Would you like to buy this medicine from an online pharmacy?")
        buy = input("\nWould you like to buy this medicine? (yes/no): ").strip().lower()

        if buy in ["yes", "y"]:
            speak("Okay! Opening the purchase link for you.")
            print("Opening link:", med_link)
            webbrowser.open(med_link)
        else:
            speak("No problem, you can buy it later if needed.")
    else:
        speak("Sorry, I don't have a suggestion for that health issue.")
        print("Sorry, I don't have a suggestion for that health issue.")

# Main program loop
def main():
    speak("Hello! Welcome to MadExpress, your friendly medicine guide.")
    
    while True:
        condition = input("\nPlease tell me your health issue: ").strip()
        suggest_medicine(condition)

        speak("Do you have another health issue to discuss?")
        more = input("\nDo you have another health issue? (yes/no): ").strip().lower()
        if more not in ["yes", "y"]:
            speak("No problem, take some rest and stay healthy!")
            print("\nMadExpress: Take care and get well soon! 💚")
            break

# Run the assistant
if __name__ == "__main__":
    main()
