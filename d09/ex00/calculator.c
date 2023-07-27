#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject* add(PyObject* self, PyObject* args) {
    double a, b;

    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }

    return Py_BuildValue("d", a + b);
}

static PyObject* sub(PyObject* self, PyObject* args) {
    double a, b;

    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }

    return Py_BuildValue("d", a - b);
}

static PyObject* mul(PyObject* self, PyObject* args) {
    double a, b;

    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }

    return Py_BuildValue("d", a * b);
}

static PyObject* divide(PyObject* self, PyObject* args) {
    double a, b;

    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }

    if (b == 0) {
        PyErr_SetString(PyExc_ZeroDivisionError, "Cannot divide by zero");
        return NULL;
    }

    return Py_BuildValue("d", a / b);
}

// методы модуля
static PyMethodDef methods[] = {
    {"add", add, METH_VARARGS, "Add two numbers"},
    {"sub", sub, METH_VARARGS, "Subtract two numbers"},
    {"mul", mul, METH_VARARGS, "Multiply two numbers"},
    {"div", divide, METH_VARARGS, "Divide two numbers"},
    {NULL, NULL, 0, NULL} // завершающий элемент массива
};

// структура модуля
static struct PyModuleDef calculator_module = {
    PyModuleDef_HEAD_INIT,
    "calculator",
    NULL,
    -1,
    methods
};

// инициализация модуля
PyMODINIT_FUNC PyInit_calculator(void) {
    return PyModule_Create(&calculator_module);
}
