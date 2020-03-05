from ..storage import db

import syft as sy


class ModelCheckPoint(db.Model):
    """ Model's save points.
        Columns:
            id (Integer, Primary Key): Checkpoint ID.
            values (Binary): Value of the model at a given checkpoint.
            model_id (String, Foreign Key): Model's ID.
    """

    __tablename__ = "__model_checkpoint__"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    values = db.Column(db.LargeBinary)
    alias = db.Column(db.String)
    model_id = db.Column(db.String, db.ForeignKey("__model__.id"), unique=True)

    @property
    def object(self):
        return sy.serde.deserialize(self.values)

    @object.setter
    def object(self):
        self.data = sy.serde.serialize(self.values)

    def __str__(self):
        return f"<CheckPoint id: {self.id} , values: {self.data}>"
