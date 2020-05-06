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
	listint_t *forward = NULL, *prev = NULL;

	while (*head)
	{
		forward = (*head)->next;
		(*head)->next = prev;
		prev = (*head);
		(*head) = forward;
	}
	(*head) = prev;
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
	listint_t *cp = *head, *cv = *head;

	if (*head == NULL)
		return (1);
	while (cv->next && cv->next->next)
	{
		cp = cp->next;
		cv = cv->next->next;
	}
	reverse_listint(&cp);
	cv = *head;
	for (; cp && cv; cp = cp->next, cv = cv->next)
		if (cv->n != cv->n)
			return (0);
	return (1);
}
