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
        #Make game start instead of end
        return render_template('start.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            # Weird, a POST request to /game wit no user input... what should your code do?
            return render_template('try_again.html')
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                #There's no transition for that user inout
                #what should your code do in response?
                tempvari =  render_template('try_again.html')
            else:
                session['scene'] = nextscene.urlname
                tempvari = render_template('show_scene.html', scene=nextscene)

            return tempvari
    else:
        #There's no session, ho could the user get here?
        # What should your code do in response?
        return render_template('you_died.html')

# This urL initializes the session with starting values
@app.route('/')
def index():
    session['scene'] = map.START.urlname
    return redirect(url_for('game_get')) # redirect the browser to the url for game_get

app.secret_key = 'salasana666'

if __name__ == "__main__":
    app.run()
