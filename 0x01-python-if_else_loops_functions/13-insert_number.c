#include "lists.h"

/**
 * insert_node - function that inserts a number into a singly-linked list
 * @head: pointer to the head of a linked list
 * @number: The number to insert
 * Return: 0 if the function fails or return the pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_node;

	 /* Allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;/**insert value to new node**/

	/* Check if the list is empty or the new node should be the new head */
	if (node == NULL || number < node->n)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}
	 /* Traverse the list to find the correct position for the new node */
	while (node->next && node->next->n < number)
		node = node->next;
	
	/* Insert the new node into the list */
	new_node->next = node->next;
	node->next = new_node;

	return (new_node);
}
