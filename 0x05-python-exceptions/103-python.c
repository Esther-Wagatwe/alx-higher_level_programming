#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - function that Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t s_ize, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	s_ize = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", s_ize);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < s_ize; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - function that prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t s_ize, i;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		s_ize = 10;
	else
		s_ize = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", s_ize);
	for (i = 0; i < s_ize; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (s_ize - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - function that prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *bffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	bffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", bffer);
	PyMem_Free(bffer);
}
