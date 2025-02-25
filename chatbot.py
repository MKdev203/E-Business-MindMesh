import random

def generate_concept_response(topic):
    """Generiert eine grobe Konzeptgliederung basierend auf dem Thema."""
    outlines = {
    "design": [
        "1. Einführung in das Designziel",
        "   - Zieldefinition und Anforderungen",
        "   - Markt- und Konkurrenzanalyse",
        "2. Farb- und Stilkonzept",
        "   - Farbpsychologie und Markenidentität",
        "   - Auswahl der Primär- und Sekundärfarben",
        "   - Schriftarten und visuelle Hierarchie",
        "3. User Experience (UX) Strategien",
        "   - Erstellung von User Personas",
        "   - Wireframing und Prototyping",
        "   - Usability-Tests und Feedback-Analyse",
        "4. Optimierung & Weiterentwicklung",
        "   - Performance-Optimierung",
        "   - Accessibility & Barrierefreiheit",
        "   - A/B-Testing für Design-Iterationen"
    ],
    "entwicklung": [
        "1. Problemstellung & Anforderungen",
        "   - Analyse der Geschäftsanforderungen",
        "   - Definition von Use Cases",
        "   - Anforderungsdokumentation",
        "2. Technologiewahl & Architektur",
        "   - Auswahl der passenden Tech-Stacks",
        "   - Systemarchitektur und Datenbanken",
        "   - Skalierbarkeit und Sicherheitsaspekte",
        "3. Implementierungsschritte",
        "   - Entwicklung der Backend-Logik",
        "   - Frontend-Entwicklung und UI-Komponenten",
        "   - API-Design und Schnittstellen",
        "4. Testing & Qualitätssicherung",
        "   - Automatisierte Tests (Unit, Integration, UI)",
        "   - Manuelle Tests und User Acceptance Tests",
        "   - Debugging und Fehlerbehebung"
    ],
    "marketing": [
        "1. Zielgruppenanalyse",
        "   - Definition der Buyer Persona",
        "   - Marktsegmentierung und Trendanalyse",
        "   - Wettbewerbsanalyse",
        "2. Werbe- & Kommunikationsstrategie",
        "   - Content-Marketing-Planung",
        "   - Social-Media-Strategie",
        "   - Influencer- & Affiliate-Marketing",
        "3. Kampagnenplanung & Umsetzung",
        "   - Planung von Multichannel-Kampagnen",
        "   - Performance Marketing (Google Ads, Meta Ads)",
        "   - E-Mail-Marketing & Retargeting",
        "4. Erfolgsmessung & Optimierung",
        "   - KPIs und Conversion-Tracking",
        "   - Analyse von Google Analytics & Heatmaps",
        "   - Optimierung durch A/B-Tests"
    ],
    "beratung": [
        "1. Ist-Analyse & Herausforderungen",
        "   - Erfassung des aktuellen Unternehmensstatus",
        "   - SWOT-Analyse (Stärken, Schwächen, Chancen, Risiken)",
        "   - Identifikation von Pain Points",
        "2. Strategische Lösungsansätze",
        "   - Entwicklung einer Roadmap für die Umsetzung",
        "   - Definition von kurz-, mittel- und langfristigen Zielen",
        "   - Integration von innovativen Technologien",
        "3. Umsetzungsplan & Meilensteine",
        "   - Festlegung von Projektphasen und Deliverables",
        "   - Ressourcen- und Budgetplanung",
        "   - Change-Management-Strategien",
        "4. Monitoring & Evaluation",
        "   - Laufende Erfolgskontrolle und Reporting",
        "   - Feedback-Schleifen und agile Anpassungen",
        "   - Nachhaltigkeits- und Skalierungsstrategien"
    ]
}

    
    topic = topic.lower()
    if topic in outlines:
        return f"Grobe Gliederung für {topic.capitalize()}:\n" + "\n".join(outlines[topic])
    else:
        return "Dieses Thema ist nicht verfügbar. Bitte wählen Sie zwischen Design, Entwicklung, Marketing oder Beratung."

def chatbot():
    print("Willkommen beim AI-gestützten Konzept-Chatbot!")
    print("Geben Sie ein Thema ein (Design, Entwicklung, Marketing, Beratung) oder 'exit' zum Beenden.")
    
    while True:
        user_input = input("Ihr Thema: ").strip().lower()
        if user_input == "exit":
            print("Danke für die Nutzung unseres Chatbots! Auf Wiedersehen.")
            break
        
        response = generate_concept_response(user_input)
        print(response)

if __name__ == "__main__":
    chatbot()
