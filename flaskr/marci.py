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

bp = Blueprint("marci", __name__)

@bp.route("/bmwseria1")
def seria1():
    """Show all the posts, most recent first."""
   
    return render_template("marci/bmw/bmwseria1.html")

@bp.route("/bmwseria2")
def seria2():
    """Show all the posts, most recent first."""
   
    return render_template("marci/bmw/bmwseria2.html")


@bp.route("/bmwseria3")
def seria3():
    """Show all the posts, most recent first."""
   
    return render_template("marci/bmw/bmwseria3.html")

@bp.route("/bmwseria4")
def seria4():
    """Show all the posts, most recent first."""
   
    return render_template("marci/bmw/bmwseria4.html")

@bp.route("/bmwseria5")
def seria5():
    """Show all the posts, most recent first."""
   
    return render_template("marci/bmw/bmwseria5.html")

@bp.route("/bmwseria6")
def seria6():
    """Show all the posts, most recent first."""
   
    return render_template("marci/bmw/bmwseria6.html")

@bp.route("/bmwseria7")
def seria7():
    """Show all the posts, most recent first."""
   
    return render_template("marci/bmw/bmwseria7.html")

@bp.route("/bmwx1")
def x1():
    """Show all the posts, most recent first."""
   
    return render_template("marci/bmw/bmwx1.html")


@bp.route("/bmwx2")
def x2():
    """Show all the posts, most recent first."""
   
    return render_template("marci/bmw/bmwx2.html")

@bp.route("/bmwx3")
def x3():
    """Show all the posts, most recent first."""
   
    return render_template("marci/bmw/bmwx3.html")

@bp.route("/bmwx4")
def x4():
    """Show all the posts, most recent first."""
   
    return render_template("marci/bmw/bmwx4.html")


@bp.route("/bmwx5")
def x5():
    """Show all the posts, most recent first."""
   
    return render_template("marci/bmw/bmwx5.html")

 

@bp.route("/bmwx6")
def x6():
    """Show all the posts, most recent first."""
   
    return render_template("marci/bmw/bmwx6.html")

@bp.route("/vwgolf5")
def vwgolf5():
    """Show all the posts, most recent first."""
   
    return render_template("marci/vw/vwgolf5.html")

@bp.route("/vwgolf6")
def vwgolf6():
    """Show all the posts, most recent first."""
   
    return render_template("marci/vw/vwgolf6.html")

@bp.route("/vwgolf7")
def vwgolf7():
    """Show all the posts, most recent first."""
   
    return render_template("marci/vw/vwgolf7.html")

@bp.route("/vwpassat")
def vwpassat():
    """Show all the posts, most recent first."""
   
    return render_template("marci/vw/vwpassat.html")

@bp.route("/vwpassatcc")
def vwpassatcc():
    """Show all the posts, most recent first."""
   
    return render_template("marci/vw/vwpassatcc.html")
    
@bp.route("/vwjetta")
def vwjetta():
    """Show all the posts, most recent first."""
   
    return render_template("marci/vw/vwjetta.html")

@bp.route("/vwpolo")
def vwpolo():
    """Show all the posts, most recent first."""
   
    return render_template("marci/vw/vwpolo.html")

@bp.route("/vwtiguan")
def vwtiguan():
    """Show all the posts, most recent first."""
   
    return render_template("marci/vw/vwtiguan.html")

@bp.route("/vwtouareg")
def vwtouareg():
    """Show all the posts, most recent first."""
   
    return render_template("marci/vw/vwtouareg.html")

@bp.route("/dacialogan")
def dacialogan():
    """Show all the posts, most recent first."""
   
    return render_template("marci/dacia/dacialogan.html")


@bp.route("/daciasandero")
def daciasandero():
    """Show all the posts, most recent first."""
   
    return render_template("marci/dacia/daciasandero.html")

@bp.route("/daciasanderostepway")
def daciasanderostepway():
    """Show all the posts, most recent first."""
   
    return render_template("marci/dacia/daciasanderostepway.html")

@bp.route("/daciaspring")
def daciaspring():
    """Show all the posts, most recent first."""
   
    return render_template("marci/dacia/daciaspring.html")

@bp.route("/daciaduster")
def daciaduster():
    """Show all the posts, most recent first."""
   
    return render_template("marci/dacia/daciaduster.html")

@bp.route("/audia1")
def audia1():
    """Show all the posts, most recent first."""
   
    return render_template("marci/audi/audia1.html")

   

@bp.route("/audia3")
def audia3():
    """Show all the posts, most recent first."""
   
    return render_template("marci/audi/audia3.html")

@bp.route("/audia4")
def audia4():
    """Show all the posts, most recent first."""
   
    return render_template("marci/audi/audia4.html")

@bp.route("/audia5")
def audia5():
    """Show all the posts, most recent first."""
   
    return render_template("marci/audi/audia5.html")

@bp.route("/audia6")
def audia6():
    """Show all the posts, most recent first."""
   
    return render_template("marci/audi/audia6.html")

@bp.route("/audia7")
def audia7():
    """Show all the posts, most recent first."""
   
    return render_template("marci/audi/audia7.html")

@bp.route("/audia8")
def audia8():
    """Show all the posts, most recent first."""
   
    return render_template("marci/audi/audia8.html")


@bp.route("/audiq2")
def audiq2():
    """Show all the posts, most recent first."""
   
    return render_template("marci/audi/audiq2.html")

@bp.route("/audiq3")
def audiq3():
    """Show all the posts, most recent first."""
   
    return render_template("marci/audi/audiq3.html")


@bp.route("/audiq5")
def audiq5():
    """Show all the posts, most recent first."""
   
    return render_template("marci/audi/audiq5.html")

@bp.route("/audiq7")
def audiq7():
    """Show all the posts, most recent first."""
   
    return render_template("marci/audi/audiq7.html")


@bp.route("/suzukiswift")
def suzukiswift():
    """Show all the posts, most recent first."""
   
    return render_template("marci/suzuki/suzukiswift.html")

@bp.route("/suzukivitara")
def suzukivitara():
    """Show all the posts, most recent first."""
   
    return render_template("marci/suzuki/suzukivitara.html")

@bp.route("/suzukiswace")
def suzukiswace():
    """Show all the posts, most recent first."""
   
    return render_template("marci/suzuki/suzukiswace.html")

@bp.route("/suzukiignis")
def suzukiignis():
    """Show all the posts, most recent first."""
   
    return render_template("marci/suzuki/suzukiignis.html")



