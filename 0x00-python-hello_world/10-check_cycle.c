#include "lists.h"

/**
 * check_cycle - Function to check if there is cycle in list
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *quick = list;
	listint_t *slow = list;

	if (!list)
		return (0);

	while (1)
	{
		if (quick->next != NULL && quick->next->next != NULL)
		{
			quick = quick->next->next;
			slow = slow->next;

			if (quick == slow) /* cycle found if nodes match*/
				return (1);
		}
		else
			return (0);
	}
}
