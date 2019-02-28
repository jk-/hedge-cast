def serialize(entity):
    data = {}
    if type(entity).__name__ == "list" and len(entity):
        data = [x.to_dict() for x in entity]
    else:
        if entity:
            data = entity.to_dict()
        else:
            data = {}

    return data
