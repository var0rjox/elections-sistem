from flask import render_template, redirect, url_for, flash, session
from forms.committee_login import Login
from services.committee_service import CommitteeService

committee_service = CommitteeService()


def login_controller():
    form = Login()
    if form.validate_on_submit():
        ci = form.ci.data
        password = form.password.data

        # Verificar en la db
        user = committee_service.get_user(ci)

        if user:
            if user.password == password:
                session["ci"] = user.ci
                return redirect(url_for("electoral_committee.profile"))
            else:
                flash("Credenciales incorrectas.", "danger")
                return redirect(url_for("electoral_committee.login"))
        else:
            flash("El usuario no esta registrado.", "danger")
            return redirect(url_for("electoral_committee.login"))

    if "ci" in session:
        return redirect(url_for("electoral_committee.profile"))

    return render_template("committee-login.html", form=form)


def profile_controller():
    if "ci" not in session:
        return redirect(url_for("electoral_committee.login"))
    return render_template("committee-profile.html")


def logout_controller():
    session.pop("ci", None)
    return redirect(url_for("electoral_committee.login"))


def load_information():
    ci = session["ci"]
    current_committee = committee_service.get_user(ci)
    return render_template("committee-profile.html", person=current_committee)
