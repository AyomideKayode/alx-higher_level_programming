#include "lists.h"

/**
 * rev_listint - Function to reverse a linked list in place.
 * @h: Pointer to the pointer of the first node in the list.
 */
void rev_listint(listint_t **h)
{
	listint_t *prev = NULL;
	listint_t *current = *h;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*h = prev;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Double pointer to the linked list.
 * Return: 1 if it is a palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	/* Check if the list is empty or has only one element */
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	/* Find the middle of the linked list using slow and fast pointers */
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	/* Reverse the second half of the linked list */
	rev_listint(&dup);

	/* Compare values of the first half with the reversed second half */
	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	/* If all values matched, it's a palindrome; otherwise, it's not */
	if (!dup)
		return (1);
	return (0);
}
