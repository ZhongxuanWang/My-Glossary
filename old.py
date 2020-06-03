


# This is sorely not usable. Just for later inference

class TODO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)

    time_created = db.Column(db.String, default=time_created_str)
    time_due = db.Column(db.String(500), nullable=False)

    # By default, the email warning is disabled
    email_warning = db.Column(db.Integer, default=0)

    def __repr__(self):
        return self.id

    def __str__(self):
        return self.__repr__()

    def get_time_color(self):
        time_dif = self.get_time_difference()
        if time_dif['days'] < 0 or time_dif['seconds'] < 0:
            return 'black'
        elif time_dif['days'] > 30:
            return "#0000ff"
        elif time_dif['days'] > 7:
            return "#0080ff"
        elif time_dif['days'] > 2:
            return '#00ff00'
        elif time_dif['days'] >= 1:
            return '#bfff00'
        # >Half day
        elif time_dif['seconds'] >= 43200:
            return "#ffff00"
        # >3h
        elif time_dif['seconds'] >= 10800:
            send_email(self)
            return "#ffbf00"
        # >1h
        elif time_dif['seconds'] >= 3600:
            send_email(self)
            return "#ff8000"
        else:
            send_email(self)
            return "#ff0000"

    def get_time_difference(self):
        return get_time_difference(datetime.strptime(self.time_due.__str__(), datetime_format))


'''
This will return a new date & time that after adding the values in time dictionaries
'''


def get_time(**time):
    # TODO could I optimize those statements using comprehension for?
    for item in ['hour', 'minute', 'day', 'month', 'year']:
        if item not in time:
            time[item] = 0
    time_now = datetime.now() + relativedelta(hours=time['hour'], minutes=time['minute'], days=time['day'],
                                              months=time['month'], years=time['year'])
    return time_now.strftime(datetime_format)


def get_time_difference(time):
    time_now = datetime.now().replace(microsecond=0)
    diff = time - time_now
    return {'days': diff.days, 'seconds': diff.seconds}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect('issues/404.html')
    elif request.method == 'GET':
        tasks = TODO.query.order_by(TODO.time_created).all()
        time_now = datetime.now().strftime(datetime_format)
        return render_template("index.html", tasks=tasks, mintime=time_now, maxtime=get_time(year=100),
                               display_time=get_time(hour=3))
    else:
        return "Invalid method: " + request.method


@app.route('/addTask/<content>/<due_date>', methods=['POST'])
def addTask(content, due_date):
    if request.method == 'POST':
        # content = request.form['content']
        try:
            datetime.strptime(due_date, datetime_format)
        except:
            print("The time is not in correct format")
        task = TODO(content=content, time_due=due_date)

        # Add to database
        try:
            db.session.add(task)
            db.session.commit()
            return redirect('/')
        except:
            print("Unable to add the task")
    else:
        return render_template('issues/unable_to.html', issue="method not applicable")


@app.route('/editTask/<int:tid>/<content>/<due_date>/<email_warning>', methods=['POST'])
def editTask(tid, content, due_date, email_warning):
    task = TODO.query.get_or_404(tid)

    # Accessing through form in edit
    task.content = content
    task.time_due = due_date
    task.email_warning = email_warning

    try:
        db.session.commit()
        return redirect('/')
    except:
        print("Unable to edit the task")


@app.route('/editTask/<int:tid>', methods=['GET'])
def edit_task_jump(tid):
    return render_template('edit.html', task=TODO.query.get_or_404(tid), maxtime=get_time(year=100))


@app.route('/cmTask/<int:tid>', methods=['GET'])
def cmTask(tid):
    if request.method == 'GET':
        task = TODO.query.get_or_404(tid)

        try:
            db.session.delete(task)
            db.session.commit()
            return redirect('/')
        except:
            return render_template('issues/unable_to.html', issue='complete the task')
    else:
        return render_template('issues/unable_to.html', issue="method not applicable")


@app.route('/setting/<email_add>', methods=['POST'])
def setting(email_add):
    write_file('email.cfg', email_add)
    return ''


@app.route('/setting/', methods=['GET'])
def setting_redirect():
    email = '' + read_file('email.cfg')
    return render_template('setting.html', email=email)


def read_file(filename):
    try:
        with open(filename) as f:
            return f.readline()
    except IOError:
        print("IO ERROR Raised. Reading file failed,")
        f = open(filename, "w")
        f.write('email@example.com')
        f.close()
        return 'content'


def write_file(filename, file_content):
    try:
        with open(filename, 'w') as f:
            f.write(file_content)
    except IOError:
        print("IO ERROR Raised. Writing file failed,")
    return ''