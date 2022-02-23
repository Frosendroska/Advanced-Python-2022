import numpy as np
import numbers


class StrMixin:
    def __str__(self):
        return str(self.val)


class WriteToFileMixin:
    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))


class SetGetMixin:
    def __get__(self):
        return self.val

    def __set__(self, new_value):
        self.val = new_value


class MatrixNumpy(np.lib.mixins.NDArrayOperatorsMixin, SetGetMixin, WriteToFileMixin, StrMixin):
    def __init__(self, value):
        self.val = np.asarray(value)

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        inputs = tuple(x.val if isinstance(x, MatrixNumpy) else x
                       for x in inputs)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.val)
