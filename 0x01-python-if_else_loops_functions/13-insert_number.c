#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - function that inserts a number into a sorted linked list
 * @head: pointer to pointer to head node
 * @number: inter value to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node,  *prev_node, *next_node;
	listint_t *temp = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	prev_node = temp;
	next_node = temp->next;
	while (prev_node != NULL)
	{
		if (new_node->n < temp->n)
		{
			new_node->next = temp;
			*head = new_node;
			return (new_node);
		}
		if (new_node->n >= prev_node->n && new_node->n <= next_node->n)
		{
			new_node->next = prev_node->next;
			prev_node->next = new_node;
			return (new_node);
		}
		prev_node = prev_node->next;
		next_node = next_node->next;
	}
	prev_node->next = new_node;
	return (new_node);
}

