#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info -  A function that prints some basic
 *							info about Python lists
 * @p: python list
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int eleme;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (eleme = 0; eleme < Py_SIZE(p); eleme++)
		printf("Element %d: %s\n", eleme, Py_TYPE(PyList_GetItem(p, eleme))->tp_name);
}


