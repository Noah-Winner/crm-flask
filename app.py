from flask import Flask, render_template, request
from datenbank import verbindung, tabelle_erstellen

app = Flask(__name__)
tabelle_erstellen()

@app.route("/")
def home():
    conn = verbindung()
    kunden = conn.execute("SELECT * FROM kunden").fetchall()
    conn.close()
    return render_template("home.html", kunden=kunden)

@app.route("/neu", methods=["GET", "POST"])
def neuer_kunde():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        telefon = request.form["telefon"]
        conn = verbindung()
        conn.execute(
            "INSERT INTO kunden (name, email, telefon) VALUES (?, ?, ?)",
            (name, email, telefon)
        )
        conn.commit()
        conn.close()
        return render_template("erfolg.html", name=name)
    return render_template("formular.html")

@app.route("/loeschen/<int:id>")
def kunde_loeschen(id):
    conn = verbindung()
    conn.execute("DELETE FROM kunden WHERE id = ?",(id,))
    conn.commit()
    conn.close()
    return render_template("erfolg.html", name="Kunde wurde erfolgreich gelöscht.")

if __name__ == "__main__":
    app.run(debug=True)