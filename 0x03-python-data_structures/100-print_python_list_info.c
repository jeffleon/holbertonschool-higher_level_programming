#include <Python.h>
/**
 * print_python_list_info - Prints basic info from python list.
 * @p: Python list.
 * Return: None.
 */
void print_python_list_info(PyObject *p)
{
	int length = Py_SIZE(p);
	int co = 0;

	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %li\n", ((PyListObject *) p)->allocated);
	for (co = 0; co < length; co++)
		printf("Element %d: %s\n", co, Py_TYPE(PyList_GetItem(p, co))->tp_name);
}
