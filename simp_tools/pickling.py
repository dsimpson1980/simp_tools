import cPickle


def load(filepath):
    with open(filepath, 'rb') as f:
        return cPickle.load(f)


def dump(obj, filepath):
    with open(filepath, 'w') as f:
        cPickle.dump(obj, f, cPickle.HIGHEST_PROTOCOL)