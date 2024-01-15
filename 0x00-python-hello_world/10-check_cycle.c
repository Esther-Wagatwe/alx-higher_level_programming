#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list || !list->next)
		return (0);/*If the list is empty or has only one node, there's no cycle*/

	while (fast != NULL && fast != NULL && fast->next != NULL)
	{
		/*if (slow == fast)
			return (1);*/
		slow = slow->next;/*Move slow pointer one step forward*/
		fast = fast->next->next;/*Move fast pointer two steps forward*/
		if (slow == fast)
			return(1);
	}

	return (0);
}
