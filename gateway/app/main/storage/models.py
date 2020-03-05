import json
import uuid
from . import db


class Plan(db.Model):
    """ Plan table that represents Syft Plans.
        Columns:
            id (Integer, Primary Key): Plan ID.
            name (String): Plan name.
            value (String): String  (List of operations)
            value_ts (String): String (TorchScript)
            is_avg_plan (Boolean) : Boolean flag to indicate if it is the avg plan
            fl_process_id (Integer, Foreign Key) : Referece to FL Process.
    """

    __tablename__ = "__plan__"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    value = db.Column(db.String())
    value_ts = db.Column(db.String())
    is_avg_plan = db.Column(db.Boolean, default=False)
    fl_process_id = db.Column(db.BigInteger, db.ForeignKey("__fl_process__.id"))

    def __str__(self):
        return (
            f"<Plan id: {self.id}, values: {self.value}, torchscript: {self.value_ts}>"
        )


class Protocol(db.Model):
    """ Protocol table that represents Syft Protocols.
        Columns:
            id (Integer, Primary Key): Protocol ID.
            name (String): protocol name.
            value: String  (List of operations)
            value_ts: String (TorchScript)
            fl_process_id (Integer, Foreign Key) : Referece to FL Process.
    """

    __tablename__ = "__protocol__"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    value = db.Column(db.String())
    value_ts = db.Column(db.String())
    fl_process_id = db.Column(db.BigInteger, db.ForeignKey("__fl_process__.id"))

    def __str__(self):
        return f"<Protocol id: {self.id}, values: {self.value}, torchscript: {self.value_ts}>"


class GridNodes(db.Model):
    """ Grid Nodes table that represents connected grid nodes.
    
        Columns:
            id (primary_key) : node id, used to recover stored grid nodes (UNIQUE).
            address: Address of grid node.
    """

    __tablename__ = "__gridnode__"

    id = db.Column(db.String(), primary_key=True)
    address = db.Column(db.String())

    def __str__(self):
        return f"< Grid Node {self.id} : {self.address}>"
