#include "lists.h"
/**
 * check_cycle - a function in C that checks if a singly linked list
 * has a cycle in it.
 * @list: head list
 * Return:0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	if (list == NULL)
		return (0);

	while (a && a->next != NULL)
	{
		b = b->next;
		a = a->next->next;
		if (b == a)
			return (1);
	}
	return (0);
}
