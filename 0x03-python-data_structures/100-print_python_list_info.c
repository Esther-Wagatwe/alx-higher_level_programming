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

	/* print size of list */
	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	/* print allocated memory for the list */
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	/* Loop through each element in the list */
	for (eleme = 0; eleme < Py_SIZE(p); eleme++)
		/* Print the type name of the element */
		printf("Element %d: %s\n", eleme, Py_TYPE(PyList_GetItem(p, eleme))->tp_name);
}


