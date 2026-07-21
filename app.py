from flask import Flask, render_template, request
from datenbank import verbindung, tabelle_erstellen

app = Flask(__name__)
tabelle_erstellen()

@app.route("/")
def home():
    suche = request.args.get("suche", "")
    conn = verbindung()
    if suche:
        kunden = conn.execute(
            "SELECT * FROM kunden WHERE name LIKE ?",
            (f"%{suche}%",)
        ).fetchall()
    else:
        kunden = conn.execute("SELECT * FROM kunden").fetchall()
    conn.close()
    return render_template("home.html", kunden=kunden, suche=suche)

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

@app.route("/bearbeiten/<int:id>", methods=["GET", "POST"])
def kunde_bearbeiten(id):
    conn = verbindung()
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        telefon = request.form["telefon"]
        conn.execute(
            "UPDATE kunden SET name = ?, email = ?, telefon = ? WHERE id = ?",
            (name, email, telefon, id)
        )
        conn.commit()
        conn.close()
        return render_template("erfolg.html", name=name)
    kunde = conn.execute("SELECT * FROM kunden WHERE id = ?", (id,)).fetchone()
    conn.close()
    return render_template("bearbeiten.html", kunde=kunde)

@app.route("/loeschen/<int:id>")
def kunde_loeschen(id):
    conn = verbindung()
    conn.execute("DELETE FROM kunden WHERE id = ?",(id,))
    conn.commit()
    conn.close()
    return render_template("erfolg.html", name="Kunde wurde erfolgreich gelöscht.")

if __name__ == "__main__":
    app.run(debug=True)