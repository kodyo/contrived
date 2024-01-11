#!/usr/bin/env python
from helpers.serializer import GenericSerializer
from models.widget import Widget
import uuid

def main():
    # Widget is just a dummy object. Initialize one to play with.
    widget = Widget(
        str(uuid.uuid4()),
        "test text"
    )

    # Print the object, will look something like
    # <models.widget.Widget object at 0x7f977b00bd30>
    print(widget)

    # Create a JSON-serialized string from the object contents
    # and print it.
    serialized = serializer.serialize(widget)
    print(serialized)

    # Write the JSON serialized object to a file.
    serializer.serialize_to_file(widget)

if __name__ == "__main__":
    # Initialize a serializer object from the GenericSerializer class.
    # GenericSerializer has an optional filename argument that it will use
    # and time you want to write output to a file.
    serializer = GenericSerializer(output_file="myoutfile.json")

    # Run the main function
    main()
