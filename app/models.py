

from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'User: {self.username}, email: {self.email}'

# @app.route('/edit_profile', methods=['GET', 'POST'])
# def edit_profile():
#     user = User.query.get(1)  # Предполагаем, что мы работаем с одним пользователем
#     form = EditProfileForm()
#     if form.validate_on_submit():
#         user.name = form.name.data
#         user.email = form.email.data
#         # Здесь в реальном приложении вы должны хэшировать пароль
#         if form.password.data:
#             user.password = form.password.data  # В реальности используйте хэширование
#         db.session.commit()
#         flash('Профиль обновлен!', 'success')
#         return redirect(url_for('index'))  # Предполагается, что у вас есть маршрут index
#     return render_template('edit_profile.html', form=form, user=user)
#
# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)