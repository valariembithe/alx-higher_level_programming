#include "lists.h"
/**
 * insert_node - inserts a number into a singly linked list
 * @head: pointer to head of linked list
 * @number: number to insert
 *
 * Return: a pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *aux1 = *head, *aux2 = *head, *aux3 = *head;
	unsigned int i = 0, idx = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{	new->next = *head;
		*head = new;
		return (new);	}

	while (aux1->next)
	{	idx++;
		aux3 = aux3->next;
		if (aux1->n > number)
		{	idx--;
			break;	}
		else if (aux1->next->next == NULL && aux3->n < number)
		{	idx++;
			break;	}
		aux1 = aux1->next;	}
	if (idx == 0)
	{	new->next = *head;
		*head = new;
		return (new);	}
	while (aux2 != NULL && i < idx - 1)
	{	aux2 = aux2->next;
		i++;	}
	if (i == idx - 1)
	{	new->next = aux2->next;
		aux2->next = new;
		return (new);
	}
	return (NULL);
}
