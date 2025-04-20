from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)
tasks = []
task_id_counter = 1

@main.route('/', methods=['GET', 'POST'])
def index():
    global task_id_counter
    if request.method == 'POST':
        task_text = request.form.get('task')
        if task_text:
            tasks.append({'id': task_id_counter, 'text': task_text})
            task_id_counter += 1
        return redirect(url_for('main.index'))
    return render_template('index.html', tasks=tasks)

@main.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('main.index'))

@main.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    new_text = request.form.get('new_task_text')
    for task in tasks:
        if task['id'] == task_id:
            task['text'] = new_text
            break
    return redirect(url_for('main.index'))
