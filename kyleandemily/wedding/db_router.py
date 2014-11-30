
class PhotologueRouter(object):
    """
    A router to control all database operations on models in the
    photologue application.
    """
    app_label = "photologue"
    using = "wedding_photo_db"
    
    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return self.using
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return self.using
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == self.app_label or obj2._meta.app_label == self.app_label:
            return True
        return None
    
    def allow_syncdb(self, db, model):
        """Make sure the apps we care about appear in the db"""
        if model._meta.app_label in ['south']:
            return True
        if db == self.using:
            return model._meta.app_label == self.app_label
        elif model._meta.app_label == self.app_label:
            return False
        return None
    
    def allow_migrate(self, db, model):
        if db == self.using:
            return model._meta.app_label == self.app_label
        elif model._meta.app_label == self.app_label:
            return False
        return None
