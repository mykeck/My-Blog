from flask import render_template,redirect
from . import main
from flask_login import login_required

@main.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()

    return render_template('index.html',posts = posts)


@main.route('/add',methods=['GET', 'POST'])
@login_required
def add():
    # add = True

    form=AddPost()

    if form.validate_on_submit():
        title = form.title.data
        subtitle = form.subtitle.data
        content = form.content.data

        post = Post(title=title, subtitle=subtitle, content=content, user_id=current_user.id, date_posted=datetime.now())

        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.post',form=form, post_id=post.id))
    return render_template('add.html', form=form)   


@main.route('/post/delete/<init:post_id>' ,methods = ['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.filter_by(id = post_id).one()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('.index', post = post, post_id = post.id))


@main.route('/comment/delete/<int:post_id>' ,methods=['GET', 'POST'])
@login_required
def delete_comment(post_id):

    post = Post.query.filter_by(id=post_id).first()
    comment = Comment.query.filter_by(post_id=post_id).first()

    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('.post_comments', comment=comment, post=post, post_id=post.id))    