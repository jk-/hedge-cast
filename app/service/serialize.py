def serialize(entity):
    data = {}
    if len(entity):
        data = [x.to_dict() for x in entity]
    else:
        data = entity.to_dict

    return data
