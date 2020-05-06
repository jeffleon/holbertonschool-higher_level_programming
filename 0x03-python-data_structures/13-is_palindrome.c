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
	for (; cp && cv; cv = cv->next, cp = cp->next)
	{
		if (cv->n != cp->n)
			return (0);
	}
	return (1);
}
