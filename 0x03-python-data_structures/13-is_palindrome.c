#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse_listint - this function reverse a link list
 * @head: its a head of linked list - (malloc'ed string)
 *
 * Return: a head of link list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *tmp = *head;
	listint_t *change = *head;

	if (*head == NULL)
		return (NULL);
	tmp = change->next;
	change->next = NULL;
	while (tmp)
	{
		change = tmp;
		tmp = tmp->next;
		change->next = *head;
		*head = change;
	}
	return (*head);
}
/**
 * is_palindrome - this function reverse a link list
 * @head: its a head of linked list - (malloc'ed string)
 *
 * Return: a head of link list
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy = *head, *head_2 = NULL, *copy_2 = NULL;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	for (; copy; copy = copy->next)
		add_nodeint_end(&head_2, copy->n);
	reverse_listint(&head_2);
	copy = *head;
	copy_2 = head_2;
	for (; copy || copy_2; copy = copy->next, copy_2 = copy_2->next)
		if (copy->n != copy_2->n)
			return (0);
	return (1);
}
