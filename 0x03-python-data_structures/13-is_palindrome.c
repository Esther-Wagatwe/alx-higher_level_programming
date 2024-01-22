#include "lists.h"
#include <stdio.h>
#include <stddef.h>

int compare_list(listint_t *head, listint_t *middle, int length);
void reverse(listint_t **head);

/**
  * is_palindrome - function that checks if singly linked list is a palindrome
  * @head: pointer to pointer of the head of the list
  *
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **head)
{
	int length, i;
	listint_t *current, *middle;

	if (head == NULL || *head == NULL)
		return (1);

	current = *head;
	middle = *head;

	for (length = 0; current != NULL; length++)
		current = current->next;

	length = length / 2;

	for (i = 1; i < length; i++)
		middle = middle->next;
	if (length % 2 != 0 && length != 1)
	{
		middle = middle->next;
		length = length - 1;
	}
	reverse(&middle);
	i = compare_list(*head, middle, length);

	return (i);
}

/**
  * compare_list - function that compares lists
  * @head: pointer to the head
  * @middle: pointer to the middle node
  * @length: length of the list
  * Return: if same 1 else 0
  */
int compare_list(listint_t *head, listint_t *middle, int length)
{
	int i;

	if (head == NULL || middle == NULL)
		return (1);
	for (i = 0; i < length; i++)
	{
		if (head->n != middle->n)
			return (0);
		head = head->next;
		middle = middle->next;
	}
	return (1);
}

/**
  * reverse - reverses a list
  * @head: pointer to the head to be reversed
  * Return: void
  */
void reverse(listint_t **head)
{
	listint_t *current, *next, *previous;

	if (head == NULL || *head == NULL)
		return;
	previous = NULL;
	current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
}
