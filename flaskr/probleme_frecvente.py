from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("probleme_frecvente", __name__)


@bp.route("/probleme_frecvente", methods=("GET", "POST"))
def index():

    db = get_db()
    error = None

    probleme_masina_query =  db.execute(
            "SELECT marca_masina, model_masina, componenta_problema FROM probleme_masini",
        ).fetchall()

    result = []
    for marca, model, componenta in probleme_masina_query:
        model_masina_query =  db.execute(
            "SELECT denumire_model, tip_caroserie, combustibil, cutie_viteze, an_aparitie, an_disparitie FROM model WHERE cod_model=?",(model,)
        ).fetchone()

        marca_masina_query = db.execute(
            "SELECT nume_marca FROM marca WHERE cod_marca=?",(marca,)
        ).fetchone()

        componenta_query = db.execute("SELECT denumire_componenta FROM componenta_problema WHERE id_componenta_problema=?",(componenta,)
        ).fetchone()

        model_masina_results = [x for x in model_masina_query]

        marca_masina_results = [x for x in marca_masina_query]

        componenta_results = [x for x in componenta_query]

        result.append(marca_masina_results + model_masina_results + componenta_results)

    print(result)
 
    """Show all the posts, most recent first."""
    return render_template("probleme_frecvente/probleme_frecvente.html", r=result)
