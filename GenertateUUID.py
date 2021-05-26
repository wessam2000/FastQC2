import uuid

def generateUUID():
    # make a UUID based on the host address and current time
    uuidOne = uuid.uuid1()
    return str(uuidOne)

