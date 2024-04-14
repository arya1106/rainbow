#include <Python.h>
#include <stdbool.h>
#include <string.h>
#include <sys/mman.h>

PyObject *py_test(PyObject *self, PyObject *args) {
    printf("Hello from C!\n");
    return PyUnicode_FromString("Hello. I'm a C function.");
}

static PyMethodDef methods[] = {
    {"test", (PyCFunction)py_test, METH_NOARGS, "Test"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef regex_module = {
    PyModuleDef_HEAD_INIT,
    "_rainbow",                              
    NULL,  
    -1,                                   
    methods,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC PyInit__rainbow() {
    printf("_regex init\n");
    return PyModule_Create(&regex_module);
};