import os

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def result():
    number = int(request.form['task'])
    if request.method == 'POST':
        open("tasks.txt", "w").close()
        with open('tasks.txt', 'a+') as f:
            for i in range(number):
                period = request.form['Periode' + str(i)]
                arival_time = request.form['At' + str(i)]
                burst_time = request.form['Bt' + str(i)]
                deadline = request.form['Deadline' + str(i)]
                nom = request.form['Nt' + str(i)]
                f.write(str(period) + " " + str(arival_time) + " " + str(burst_time) + " " + str(deadline) + " " + str(nom) + "\n")

    algo = request.form['algo']
    if algo == "rm":
        os.system('python algorithms/RM/rm.py')
        return render_template('rm.html')
    elif algo == "dm":
        os.system('python algorithms/DM/dm.py')
        return render_template('dm.html')
    elif algo == "llf":
        os.system('python algorithms/LLF/llf.py')
        return render_template('llf.html')
    else:
        os.system('python algorithms/EDF/edf.py')
        return render_template('edf.html')


if __name__ == '__main__':
    app.run(debug=True)
