from models import posts, db, comments, comments_flag

class post_repository:

    def get_all_posts():
        if posts:
            return posts.query.all()    
        else:
            return None
    
    def get_post_by_id(self, post_id):
        return posts.query.get(post_id)

    def create_post(post_id, post_title, post_link, post_text, post_rating):
        # Use the class.
        new_post = posts(post_id = post_id, post_title=post_title, post_link=post_link, post_text=post_text, post_rating=post_rating)
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



    def flag_comments(comment_id):
        with comments_flag:
            comment = db.session.add(comment_id)
        
        return comment