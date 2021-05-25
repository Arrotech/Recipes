from sqlalchemy import inspect
from app.extensions import db

# write your models here
class Recipe(db.Model):
    """Create the recipe model."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    steps = db.Column(db.String(500), nullable=False)

    def as_dict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        """Print recipe."""
        return f"Recipe('{self.title}', '{self.ingredients}', '{self.steps}')"
