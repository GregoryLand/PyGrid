from ..storage import db


class Model(db.Model):
    """ Model table that represents the AI Models.
        Columns:
            id (String, Primary Key) : Model's id, used to recover stored model.
            version (String) : Model version.
            checkpoints (ModelCheckPoint) : Model Checkpoints. (One to Many relationship)
            fl_process_id (Integer, ForeignKey) : FLProcess Foreign Key.
    """

    __tablename__ = "__model__"

    id = db.Column(db.String, primary_key=True)
    version = db.Column(db.String())
    checkpoints = db.relationship("ModelCheckPoint", backref="checkpoint")
    fl_process_id = db.Column(
        db.BigInteger, db.ForeignKey("__fl_process__.id"), unique=True
    )

    def __str__(self):
        return f"<Model  id: {self.id}, version: {self.version}>"
