from flask import session, render_template, redirect, url_for, flash

from forms.voter_login import VoterLogin
from services.voters_service import VotersServices


votersService = VotersServices()


def login_controller():
    if "ci" in session:
        return redirect(url_for("home.voter_profile"))

    form = VoterLogin()
    is_form_valid = form.validate_on_submit()

    if not is_form_valid:
        for _, errors in form.errors.items():
            for error in errors:
                flash(f"{error}", "danger")

        return render_template("voter-login.html", form=form)

    if is_form_valid:
        ci = form.ci.data
        user = votersService.get_single_voter(ci)

        if not user:
            flash(
                "El número de cédula no está registrado en el padrón electoral",
                "danger",
            )
            return redirect(url_for("home.login"))

        birdate_match = user.birthdate == form.birthdate.data

        if not birdate_match:
            flash("La fecha de nacimiento no coincide", "danger")
            return redirect(url_for("home.login"))

        if not user.is_enabled:
            flash(
                "Usted no está habilitado para votar, debido a que ya ejerció su derecho al voto",
                "danger",
            )
            return redirect(url_for("home.login"))

        session["ci"] = ci
        return redirect(url_for("home.voter_profile"))

    return render_template("voter-login.html", form=form)


def voter_profile_controller():
    if "ci" not in session:
        flash("Debe iniciar sesión para poder votar", "danger")
        return redirect(url_for("home.login"))
    else:
        return redirect(url_for("voter.index"))


def voter_logout_controller():
    session.pop("ci", None)
    return redirect(url_for("home.login"))
