#include "lists.h"

/**
* insert_node - a function in C that inserts a number into a sorted
* singly linked list.
* @head:list head
* @number: number of list to insert
* Return:the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *a = *head;
	listint_t *b = malloc(sizeof(listint_t));

	if (b == NULL)
		return (NULL);

	b->n = number;

	if (a == NULL || a->n >= number)
	{
		b->next = a;
		*head = b;
		return (b);
	}

	while (a && a->next && a->next->n < number)
		a = a->next;

	b->next = a->next;
	a->next = b;

	return (b);
}
