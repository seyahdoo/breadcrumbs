from bson import ObjectId


def object_stringify(d):
    tochange = {}
    for k, v in d.items():
        if isinstance(v, dict):
            tochange[k] = object_stringify(v)

        if isinstance(v, list):
            newlist = []
            for i in v:
                newlist.append(str(i))
            tochange[k] = newlist

        if isinstance(v, ObjectId):
            print("more objectid")
            tochange[k] = str(v)

    for k, v in tochange.items():
        d[k] = v

    return d
