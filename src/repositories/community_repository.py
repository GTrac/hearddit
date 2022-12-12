from src.models import community, db

class community_repository:

    def get_all_coms(self):
        return community.query.all()

    
    def get_com_by_id(self, com_id):
        return community.query.get(com_id)

    def create_com(com_name, user_id):
        # Use the class coms to complete this function.
        new_community = community(com_name=com_name, user_id=user_id)
        db.session.add(new_community)
        db.session.commit()
        return new_community
    
    # Works best if it uses a title.
    def search_com(self, com_name):
        search = db.session.query(com_name)
        if com_name:
            return search
        else:
            return None

    # Needs a com_id for this to be possible.
    def delete_com(com_id):
        db.session.delete(com_id)
        db.session.commit()
        return com_id



com_singleton = community_repository()