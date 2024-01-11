import json


class GenericSerializer():
    def __init__(self, output_file="outfile.json"):
        self.outfile = output_file

    def serialize(self, myobject: object):
        return json.dumps(myobject.__dict__, indent=2)
    
    def serialize_to_file(self, myobject: object):
        with open(self.outfile, 'w') as f:
            f.write(json.dumps(myobject.__dict__, indent=2))
