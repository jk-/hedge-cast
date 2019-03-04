from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Repository(object):
    """A :class:`Repository` instance encapsulates common SQLAlchemy model
    operations in the context of a :class:`Flask` application.
    """

    __model__ = None

    @classmethod
    def _isinstance(cls, model, raise_error=True):
        """Checks if the specified model instance matches the service's model.
        By default this method will raise a `ValueError` if the model is not the
        expected type.
        :param model: the model instance to check
        :param raise_error: flag to raise an error on a mismatch
        """
        rv = isinstance(model, cls.__model__)
        if not rv and raise_error:
            raise ValueError("%s is not of type %s" % (model, cls.__model__))
        return rv

    @classmethod
    def _preprocess_params(cls, kwargs):
        """Returns a preprocessed dictionary of parameters. Used by default
        before creating a new instance or updating an existing instance.
        :param kwargs: a dictionary of parameters
        """
        kwargs.pop("csrf_token", None)
        return kwargs

    @classmethod
    def save(cls, model):
        """Commits the model to the database and returns the model
        :param model: the model to save
        """
        cls._isinstance(model)
        db.session.add(model)
        db.session.commit()
        return model

    @classmethod
    def all(cls):
        """Returns a generator containing all instances of the service's model.
        """
        return cls.__model__.query.all()

    @classmethod
    def get(cls, id):
        """Returns an instance of the service's model with the specified id.
        Returns `None` if an instance with the specified id does not exist.
        :param id: the instance id
        """
        return cls.__model__.query.get(id)

    @classmethod
    def get_all(cls, *ids):
        """Returns a list of instances of the service's model with the specified
        ids.
        :param *ids: instance ids
        """
        return cls.__model__.query.filter(cls.__model__.id.in_(ids)).all()

    @classmethod
    def find(cls, **kwargs):
        """Returns a list of instances of the service's model filtered by the
        specified key word arguments.
        :param **kwargs: filter parameters
        """
        return cls.__model__.query.filter_by(**kwargs)

    @classmethod
    def first(cls, **kwargs):
        """Returns the first instance found of the service's model filtered by
        the specified key word arguments.
        :param **kwargs: filter parameters
        """
        return cls.find(**kwargs).first()

    @classmethod
    def get_or_404(cls, id):
        """Returns an instance of the service's model with the specified id or
        raises an 404 error if an instance with the specified id does not exist.
        :param id: the instance id
        """
        return cls.__model__.query.get_or_404(id)

    @classmethod
    def new(cls, **kwargs):
        """Returns a new, unsaved instance of the service's model class.
        :param **kwargs: instance parameters
        """
        return cls.__model__(**cls._preprocess_params(kwargs))

    @classmethod
    def create(cls, **kwargs):
        """Returns a new, saved instance of the service's model class.
        :param **kwargs: instance parameters
        """
        return cls.save(cls.new(**kwargs))

    @classmethod
    def update(cls, model, **kwargs):
        """Returns an updated instance of the service's model class.
        :param model: the model to update
        :param **kwargs: update parameters
        """
        cls._isinstance(model)
        for k, v in cls._preprocess_params(kwargs).items():
            setattr(model, k, v)
        cls.save(model)
        return model

    @classmethod
    def delete(cls, model):
        """Immediately deletes the specified model instance.
        :param model: the model instance to delete
        """
        cls._isinstance(model)
        db.session.delete(model)
        db.session.commit()
