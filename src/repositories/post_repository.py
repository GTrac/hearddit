from src.models import posts, db

class post_repository:

    def get_all_posts(self):
        if posts:
            return posts.query.all()    
        else:
            return None
    
    def get_post_by_id(self, post_id):
        return posts.query.get(post_id)

    def get_post_by_com(self, com_id):
        search = posts.query.filter(posts.com_id == com_id).all()
        if com_id:
            return search
        else:
            return None

    def create_post(post_title, post_link, post_text):
        # Use the class posts to complete this function.
        new_post = posts(post_title=post_title, post_link=post_link, post_text=post_text, post_rating=1)
        db.session.add(new_post)
        db.session.commit()
        return new_post
    
    # Works best if it uses a title.
    def search_post(self, title):
        search = db.session.query(title)

        if title:
            return search
        else:
            return None

    # Needs a post_id for this to be possible.
    def delete_post(post_id):
        db.session.delete(post_id)
        db.session.commit()
        return post_id



post_singleton = post_repository()