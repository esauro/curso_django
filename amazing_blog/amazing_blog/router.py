

class OddRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if "instance" in hints and hasattr(hints["instance"], "id"):
            if not hints["instance"].id % 2:
                return "odd"
            else:
                return "default"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        print hints
        if "instance" in hints and hasattr(hints["instance"], "id"):
            if not hints["instance"].id % 2:
                return "odd"
            else:
                return "default"
        return None