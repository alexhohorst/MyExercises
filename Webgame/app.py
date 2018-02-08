from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map


app = Flask(__name__)


@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        return render_template('death.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if'scene' in session:
        if userinput is None:
            return render_template('death.html')
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                return render_template('death.html')
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:
        return render_template('death.html')

@app.route('/')
def start():
    session['scene'] = map.START.urlname
    return redirect(url_for('game_get'))

app.secret_key = 'replace'

if __name__ == "__main__":
    app.run(port = 5000)
