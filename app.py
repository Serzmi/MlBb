from flask import Flask, render_template, abort
import json

app = Flask(__name__)

def load_heroes():
    with open('data/heroes.json', 'r', encoding='utf-8') as f:
        heroes = json.load(f)
    return heroes

@app.route('/')
def index():
    return render_template('main_page/main_page.html')

@app.route('/heroes')
def heroesPage():
    heroes = load_heroes()
    return render_template('heroes/heroes.html', heroes=heroes)

@app.route('/hero/<int:hero_id>')
def hero_detail(hero_id):
    heroes = load_heroes()
    hero_name = heroes.get(str(hero_id))
    if not hero_name:
        abort(404)
    hero = {
        'id': hero_id,
        'name': hero_name,
        'image': f'{hero_id}.webp'
    }
    return render_template('hero_detail/hero_detail.html', hero=hero)

if __name__ == '__main__':
    app.run(debug=True)
