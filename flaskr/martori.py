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

bp = Blueprint("martori", __name__)


@bp.route("/martori", methods=("GET", "POST"))
def index():
    """Show all the posts, most recent first."""
    return render_template("martori/martori.html")

@bp.route("/martori/pagina_martori/problmotor", methods=("GET", "POST"))
def problmotor():
    """Show all the posts, most recent first."""
    return render_template("martori/pagina_martori/problmotor.html")

@bp.route("/martori/apacombustibil", methods=("GET", "POST"))
def apacombustibil():
    """Show all the posts, most recent first."""
    return render_template("martori/apacombustibil.html")

@bp.route("/martori/dezghetareluneta", methods=("GET", "POST"))
def dezghetareluneta():
    """Show all the posts, most recent first."""
    return render_template("martori/dezghetareluneta.html")

@bp.route("/martori/dezghetareparbriz", methods=("GET", "POST"))
def dezghetareparbriz():
    """Show all the posts, most recent first."""
    return render_template("martori/dezghetareparbriz.html")

@bp.route("/martori/senzoriploaie", methods=("GET", "POST"))
def senzoriploaie():
    """Show all the posts, most recent first."""
    return render_template("martori/senzoriploaie.html")

@bp.route("/martori/probldecapotabil", methods=("GET", "POST"))
def probldecapotabil():
    """Show all the posts, most recent first."""
    return render_template("martori/probldecapotabil.html")

@bp.route("/martori/probladaptive", methods=("GET", "POST"))
def probladaptive():
    """Show all the posts, most recent first."""
    return render_template("martori/probladaptive.html")

@bp.route("/martori/defectcabluri", methods=("GET", "POST"))
def defectcabluri():
    """Show all the posts, most recent first."""
    return render_template("martori/defectcabluri.html")


@bp.route("/martori/vizitaservice", methods=("GET", "POST"))
def vizitaservice():
    """Show all the posts, most recent first."""
    return render_template("martori/vizitaservice.html")

@bp.route("/martori/airbagdezactivat", methods=("GET", "POST"))
def airbagdezactivat():
    """Show all the posts, most recent first."""
    return render_template("martori/airbagdezactivat.html")

@bp.route("/martori/filtruparticule", methods=("GET", "POST"))
def filtruparticule():
    """Show all the posts, most recent first."""
    return render_template("martori/filtruparticule.html")

@bp.route("/martori/coborarepanta", methods=("GET", "POST"))
def coborarepanta():
    """Show all the posts, most recent first."""
    return render_template("martori/coborarepanta.html")

@bp.route("/martori/becfrana", methods=("GET", "POST"))
def becfrana():
    """Show all the posts, most recent first."""
    return render_template("martori/becfrana.html")

@bp.route("/martori/becars", methods=("GET", "POST"))
def becars():
    """Show all the posts, most recent first."""
    return render_template("martori/becars.html")

@bp.route("/martori/apasareambreiaj", methods=("GET", "POST"))
def apasareambreiaj():
    """Show all the posts, most recent first."""
    return render_template("martori/apasareambreiaj.html")



@bp.route("/martori/problemeesp", methods=("GET", "POST"))
def problemeesp():
    """Show all the posts, most recent first."""
    return render_template("martori/problemeesp.html")

@bp.route("/martori/senzorlumina", methods=("GET", "POST"))
def senzorlumina():
    """Show all the posts, most recent first."""
    return render_template("martori/senzorlumina.html")

@bp.route("/martori/modiarna", methods=("GET", "POST"))
def modiarna():
    """Show all the posts, most recent first."""
    return render_template("martori/modiarna.html")


@bp.route("/martori/presiunescazuta", methods=("GET", "POST"))
def presiunescazuta():
    """Show all the posts, most recent first."""
    return render_template("martori/presiunescazuta.html")












