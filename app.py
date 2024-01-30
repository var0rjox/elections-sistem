from flask import Flask

from routes.home import home
from routes.user import user
from routes.election_results import election_results
from routes.committee import electoral_committee
from routes.voter import voter
from routes.send_vote import send_vote
from pipes.sort_report import sort_report

app = Flask(__name__)
app.secret_key = "mysecretkey"

app.register_blueprint(home)
app.register_blueprint(user)
app.register_blueprint(election_results)
app.register_blueprint(electoral_committee)
app.register_blueprint(voter)
app.register_blueprint(send_vote)

app.add_template_filter(sort_report)

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
