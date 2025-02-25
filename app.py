from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from chatbot import generate_concept_response


app = Flask(__name__, static_folder="static", template_folder="templates")

# Konfiguration der SQLite-Datenbank
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///brainstorming.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Datenbankmodell für Ideen
class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

# Datenbank erstellen
with app.app_context():
    db.create_all()

@app.route("/")
def home():
   return render_template('index.html')

@app.route("/brainstorming", methods=["GET", "POST"])
def brainstorming():
    if request.method == "POST":
        idea_text = request.form.get("idea")
        if idea_text:
            new_idea = Idea(content=idea_text)
            db.session.add(new_idea)
            db.session.commit()
    ideas = Idea.query.all()  # Ideen aus der Datenbank abrufen
    return render_template('brainstorming.html', ideas=ideas)

@app.route("/delete_idea/<int:idea_id>")
def delete_idea(idea_id):
    idea = Idea.query.get(idea_id)
    if idea:
        db.session.delete(idea)
        db.session.commit()
    return redirect(url_for('brainstorming'))

@app.route('/ueber-uns')
def ueber_uns():
    return render_template('ueber-uns.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

@app.route('/beratung')
def beratung():
    return render_template('beratung.html')

@app.route('/marketing')
def marketing():
    return render_template('marketing.html')

@app.route('/entwicklung')
def entwicklung():
    return render_template('entwicklung.html')

@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/produkte')
def produkte():
    return render_template('produkte.html')

@app.route("/chatbot", methods=["POST"])
def chatbot_response():
    data = request.get_json()
    topic = data.get("topic", "").lower()
    response = generate_concept_response(topic)
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=True)
