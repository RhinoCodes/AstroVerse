import json


class shelve:
    def __init__(self, name):
        self.name = name + '.json'
        try:
            eval(open(self.name).read())
        except:
            open(self.name, "w+").write("{}")

    def __getitem__(self, slice):
        try:
            return eval(open(self.name).read())[slice]
        except:
            return None

    def __delitem__(self, slice):
        c = open(self.name)
        data = eval(c.read())
        c.close()
        with open(self.name, "w+") as f:
            del data[slice]
            f.write(json.dumps(data))

    def __setitem__(self, slice, value):
        c = open(self.name)
        data = eval(c.read())
        c.close()
        with open(self.name, "w+") as f:
            data[slice] = value
            f.write(json.dumps(data))

    def __repr__(self):
        return open(self.name).read()
