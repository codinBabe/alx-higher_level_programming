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
	listint_t *a, *c;	
	listint_t *b = malloc(sizeof(listint_t));

	if (head == NULL)
		return (NULL);

	if (b == NULL)
		return (NULL);

	b->n = number;
	c = NULL;
	a = *head;

	if (*head == NULL || number <= (*head)->n)
	{
		b->next = *head;
		*head = b;
		return (b);
	}

	a = *head;
	while (a->next != NULL && a->next->n < number)
		a->next = b;

	b->next = a->next;
	a->next = b;

	return (b);
}
