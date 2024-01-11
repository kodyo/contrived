import json


class GenericSerializer():
    def __init__(self, output_file="outfile.json"):
        self.outfile = output_file

    def serialize(self, myobject: object):
        '''
        Return JSON string dumped from the object contents
        '''
        return json.dumps(myobject.__dict__, indent=2)
    
    def serialize_to_file(self, myobject: object):
        '''
        Write dumped JSON string to the file specified when
        GenericSerializer class is initialized.
        '''
        with open(self.outfile, 'w') as f:
            f.write(json.dumps(myobject.__dict__, indent=2))
