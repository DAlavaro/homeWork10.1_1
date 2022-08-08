from flask import Flask
from utils import all_candidates, get_by_pk, get_by_skill, load_candidates

app = Flask(__name__)
data = load_candidates()

@app.route('/')
def index():
    text = '<pre>'
    for i in range(len(data)):
        text += f'{data[i]["name"]} -\n{data[i]["pk"]}\n{data[i]["skills"]}\n\n'
    text += '</pre>'
    return text

@app.route('/candidates/<int:pk>/')
def candidates(pk):
    """
    Выводит данные кандидата
    """
    user, picture, skills = get_by_pk(pk)
    text = f"<img src='({picture})'>"
    text +=f"<pre>{user} -\n{pk}\n{skills}</pre>"
    return text

@app.route('/skills/<x>')
def skills(x):
    """
    Выведите тех кандидатов, в списке навыков у которых содержится skill
    """
    name = get_by_skill(x)
    text = '<pre>'
    for i in data:
        for j in name:
            if i['name'] == j:
                text += f"{i['name']} -\n{i['pk']}\n{i['skills']}\n\n"
    text += '</pre>'
    return text


if __name__ == '__main__':
    app.run(port=5000)

