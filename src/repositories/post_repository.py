from src.models import posts, db, user_comments, flag_comments

class post_repository:

    def get_all_posts(self):
        if posts:
            return posts.query.all()    
        else:
            return None
    
    def get_post_by_id(self, post_id):
        return posts.query.get(post_id)

    def create_post(post_title, post_link, post_text):
        # Use the class posts to complete this function.
        new_post = posts(post_title=post_title, post_link=post_link, post_text=post_text, post_rating=1)
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

    def create_comment(comment_text, flagged_comment):
        # Use comments class.
        new_comment = user_comments(comment_text=comment_text, flagged_comment=flagged_comment)
        db.session.add(new_comment)
        db.session.commit()
        # Add to flagged database if it's a flagged comment.
        if flagged_comment == True:
            new_flagged_comment = flag_comments(flagged_comment=new_comment)
            db.session.add(new_flagged_comment)
            db.session.commit()
            return new_flagged_comment
        return new_comment

post_singleton = post_repository()
