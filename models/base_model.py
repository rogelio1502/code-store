from . import db
from utils.Exceptions import BadRequestException


class Base(object):

    @classmethod 
    def get_all(_class):

        objects = _class.query.all()
        objects_json = []

        for i in objects:
            objects_json.append(i.serialize)

        return objects_json

    @classmethod
    def insert(_class,data):
        
        obj = _class()
        for i in data:
            setattr(obj, i, data[i])
        db.session.add(obj)
        db.session.commit()
        
    
        return obj.serialize
    
    @classmethod
    def delete(_class,id):
        obj = _class()
        obj_query = obj.query.filter_by(id=id).first()


        try:
            db.session.delete(obj_query)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise BadRequestException(str(e))
        else:
            return True

    @classmethod 
    def update(_class, data):
        
        obj = _class()

        try:
            obj_query = obj.query.filter_by(id=data['id']).first()
            if obj_query is not None:

                for i in data:
                    if i != "id":
                        setattr(obj_query, i, data[i])
            else:
                raise BadRequestException(f"Does not exist a row with id {data['id']}")

        except Exception as e:
            raise BadRequestException(str(e))

        try:
            db.session.commit()
        except Exception as e:
            raise BadRequestException(str(e))
        return obj_query.serialize

    @classmethod
    def get(_class, id):
        obj = _class()

        obj_query = obj.query.filter_by(id=id).first()

        if obj_query is not None:
            return obj_query.serialize
        return {}
    
    