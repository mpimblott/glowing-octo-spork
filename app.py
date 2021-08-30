from flask import Flask, render_template, request
import os
import random
import csv


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('under_construction.html')


@app.route('/civ', methods=['GET', 'POST'])
def civ():
    if request.method == 'POST':
        no_players = int(request.form.get("no_players"))
        no_choices = int(request.form.get("no_choices"))
        civ_selection = request.form.get("civ_selection")
        civ_data = []
        result = []
        with open(os.path.join(os.path.dirname(__file__), 'civ_data.txt')) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                    print(no_players)
                    print(civ_selection)
                else:
                    if civ_selection == "New Only":
                        print(row[1])
                        print(type(row[1]))
                        if row[1] == "1":
                            civ_data.append(row[0])
                            line_count += 1
                    else:
                        civ_data.append(row[0])
                        line_count += 1
            print(f'Processed {line_count - 1} lines.')
            selection = random.sample(range(0, line_count - 1), no_players*no_choices)
            for i in selection:
                result.append(civ_data[i])

        return render_template('civ.html', no_players=no_players, civ_selection=civ_selection, civ_result=result)
    else:
        return render_template('civ.html')


# set secret for session
app.secret_key = os.urandom(50)

if __name__ == '__main__':
    app.run()
