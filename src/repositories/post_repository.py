<<<<<<< HEAD
from models import posts, db, comments, comments_flag
=======
from src.models import posts, db
>>>>>>> main

class post_repository:

    def get_all_posts(self):
        if posts:
            return posts.query.all()    
        else:
            return None
    
    def get_post_by_id(self, post_id):
        return posts.query.get(post_id)

<<<<<<< HEAD
    def create_post(post_id, post_title, post_link, post_text, post_rating, sub_id):
        # Use the class.
        new_post = posts(post_id = post_id, post_title=post_title, post_link=post_link, post_text=post_text, post_rating=post_rating, sub_id=sub_id)
=======
    def create_post(post_title, post_link, post_text):
        # Use the class posts to complete this function.
        new_post = posts(post_title=post_title, post_link=post_link, post_text=post_text, post_rating=1)
>>>>>>> main
        db.session.add(new_post)
        db.session.commit()
        return new_post
    
    
    def search_post(self, title):
        search = db.session.query(title)

        if title:
            return search
        else:
            return None

    
    def delete_post(post_id):
        db.session.delete(post_id)
        db.session.commit()
        return post_id


<<<<<<< HEAD
    def create_comments(comment_id, user_id, post_id, reply_id, flagged_comment, comment_text, comment_rating):
        # Use comments class.
        new_comment = comments(comment_id=comment_id, user_id=user_id, post_id=post_id,reply_id=reply_id, flagged_comment=flagged_comment, comment_text=comment_text, comment_rating=comment_rating)
        db.session.add(new_comment)
        db.session.commit()
        # Check if it's flagged.
        if new_comment in comments_flag.flagged_comment == True:
            new_flagged_comment = comments_flag(new_comment=flagged_comment)
            db.session.add(new_flagged_comment)
            db.session.commit()
            return new_flagged_comment
        return new_comment
=======

post_singleton = post_repository()
>>>>>>> main
