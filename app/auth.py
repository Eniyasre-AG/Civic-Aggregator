from flask import session, redirect, render_template, request, url_for

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

def login_route(app):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            if (request.form['username'] == ADMIN_USERNAME and 
                request.form['password'] == ADMIN_PASSWORD):
                session['admin'] = True
                return redirect('/dashboard')
        return render_template('login.html')
    
    @app.route('/logout')
    def logout():
        session.pop('admin', None)
        return redirect('/login')
